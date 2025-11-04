# api.py (FINAL, DEFINITIVE FIX)

from fastapi import FastAPI
import joblib
import pandas as pd
import numpy as np
import os
from .schemas import PreMatchPredictionInput, LivePredictionInput 

# --- Configuration (Paths to Saved Models) ---
MODEL_PRE_MATCH_PATH = 'models/xgb_pre_match_model_v6_tuned.joblib' 
MODEL_LIVE_PATH = 'models/xgb_live_match_model.joblib' 

app = FastAPI(
    title="CricPulse Prediction API",
    description="Serves predictions for Pre-Match Analysis and Live Win Probability (WPA).",
    version="1.0.0"
)

# --- Model Loading ---
# (Assume joblib.load runs successfully)
pre_match_model = joblib.load(MODEL_PRE_MATCH_PATH)
live_model = joblib.load(MODEL_LIVE_PATH) 


# --- Helper Function for Pre-Match Prediction (V6) ---
def preprocess_and_predict_pre_match(data: PreMatchPredictionInput):
    # 1. Convert Pydantic model to DataFrame row
    df = pd.DataFrame([data.model_dump()])
    
    # 2. Rename columns for the XGBoost model (CRITICAL FIX: Use the snake_case input names)
    # We rename the Python variable names to the expected Title Case names ONLY IN THE DATAFRAME
    df.rename(columns={
        'hist_win_pct_diff': 'Hist_Win_Pct_Diff',
        'form_diff': 'Form_Diff',
        'venue_bias_delta': 'Venue_Bias_Delta'
    }, inplace=True) 

    # 3. One-Hot Encode 'toss_decision'
    df['toss_decision_field'] = np.where(df['toss_decision'] == 'field', 1, 0)
    df = df.drop(columns=['toss_decision'])
    
    # 4. Select and order the final feature columns (CRITICAL: Use the renamed columns)
    features = df[['Hist_Win_Pct_Diff', 'Form_Diff', 'Venue_Bias_Delta', 'toss_decision_field']]
    
    # 5. Predict and cast to standard Python float for serialization
    prediction_proba = float(pre_match_model.predict_proba(features)[:, 1][0])
    
    return {
        "prediction_probability": round(prediction_proba, 4),
        "prediction_winner": "Team 1" if prediction_proba >= 0.5 else "Team 2"
    }

# --- Helper Function for Live Prediction (WPA) ---
def preprocess_and_predict_live(data: LivePredictionInput):
    # ... (DataFrame creation and feature selection logic) ...
    df = pd.DataFrame([data.model_dump()])
    
    # Feature ordering (MUST match live training order)
    # The Live Model features are naturally snake_case and should be fine, but we ensure order.
    features = df[['cumulative_runs', 'current_over', 'run_rate', 'balls_remaining']]

    # FIX: Predict and cast to standard Python float for serialization
    prediction_proba = float(live_model.predict_proba(features)[:, 1][0])
    
    return {
        "win_probability": round(prediction_proba, 4),
        "prediction_time": "In-Play (Ball-by-Ball)"
    }


# --- API Endpoints ---
@app.post("/predict/pre_match", tags=["Prediction"])
def predict_pre_match(data: PreMatchPredictionInput):
    return preprocess_and_predict_pre_match(data)

@app.post("/predict/live_wpa", tags=["Prediction"])
def predict_live_wpa(data: LivePredictionInput):
    return preprocess_and_predict_live(data)

# --- You must restart the server after this fix ---