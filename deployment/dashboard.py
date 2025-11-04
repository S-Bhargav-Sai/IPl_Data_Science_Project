# dashboard.py

import streamlit as st
import requests
import json

# --- Configuration (API Endpoints) ---
API_BASE_URL = "http://127.0.0.1:8000"
PRE_MATCH_URL = f"{API_BASE_URL}/predict/pre_match"
LIVE_WPA_URL = f"{API_BASE_URL}/predict/live_wpa"

st.set_page_config(page_title="IPL MLOps Dashboard", layout="wide")


# --- Helper Function to Call API ---
def get_prediction(url, data):
    try:
        response = requests.post(url, json=data)
        response.raise_for_status() 
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"API Connection Error: Ensure FastAPI is running at {API_BASE_URL}")
        st.code(f"Details: {e}", language='text')
        return None


# --- Streamlit UI: Page Navigation ---
st.sidebar.title(" Modules")
app_mode = st.sidebar.selectbox("Select Prediction Module", ["Pre-Match Analysis (V6)", "Live Match Win Probability (WPA)"])


# --- PRE-MATCH PREDICTION PAGE ---
if app_mode == "Pre-Match Analysis (V6)":
    st.title("🏏 Pre-Match Prediction Engine")
    st.markdown("Predict the winner based on strategic differentials. Accuracy: ~55.7%")
    st.caption("Inputs are **Differential** (Team 1 value minus Team 2 value).")

    with st.form("pre_match_form"):
        st.subheader("Match Features")
        
        # 1. Historical Win % Differential
        hist_win_pct_diff = st.slider("Historical Win % Diff:", min_value=-15.0, max_value=15.0, value=3.0, step=0.5)
        # 2. Recency/Form Differential
        form_diff = st.slider("Recent Form Diff (Last 5 Games):", min_value=-1.0, max_value=1.0, value=0.1, step=0.05)
        # 3. Venue Bias Differential
        venue_bias_delta = st.slider("Venue Bias Delta (Defend - Chase):", min_value=-10.0, max_value=10.0, value=1.5, step=0.5)
        # 4. Toss Decision
        toss_decision = st.radio("Toss Winner's Choice:", ('field', 'bat'), horizontal=True)
        
        submitted = st.form_submit_button("Get Prediction")

    if submitted:
        input_data = {
            "hist_win_pct_diff": hist_win_pct_diff, "form_diff": form_diff, 
            "venue_bias_delta": venue_bias_delta, "toss_decision": toss_decision
        }
        prediction_result = get_prediction(PRE_MATCH_URL, input_data)
        
        if prediction_result and 'prediction_probability' in prediction_result:
            proba = prediction_result['prediction_probability']
            
            st.subheader("Prediction")
            if proba >= 0.5:
                st.success(f"Team 1 Win Probability: **{proba * 100:.2f}%**")
            else:
                st.error(f"Team 2 Win Probability: **{(1.0 - proba) * 100:.2f}%**")


# --- LIVE WPA PREDICTION PAGE ---
elif app_mode == "Live Match Win Probability (WPA)":
    st.title("⚡ Live Match Win Probability (WPA)")
    st.markdown("Tracks the Chasing Team's probability after every ball in the 2nd Innings.")

    with st.form("live_prediction_form"):
        st.subheader("Current Game State (2nd Innings)")
        
        # Input 1: Cumulative Runs
        cumulative_runs = st.number_input("Runs Scored by Chasing Team:", min_value=0, value=75, step=1)
        # Input 2: Current Over
        current_over = st.number_input("Completed Overs:", min_value=0, max_value=19, value=8)
        # Input 3: Run Rate
        run_rate = st.slider("Current Run Rate (RPO):", min_value=4.0, max_value=12.0, value=7.5, step=0.1)
        # Input 4: Balls Remaining
        balls_remaining = st.number_input("Balls Remaining:", min_value=1, max_value=120, value=75) 
        
        submitted_live = st.form_submit_button("Get Live WPA")

    if submitted_live:
        input_data_live = {
            "cumulative_runs": float(cumulative_runs),
            "current_over": float(current_over),
            "run_rate": float(run_rate),
            "balls_remaining": int(balls_remaining)
        }
        
        prediction_result_live = get_prediction(LIVE_WPA_URL, input_data_live)
        
        if prediction_result_live and 'win_probability' in prediction_result_live:
            proba_win = prediction_result_live['win_probability']
            
            st.subheader("Current Win Probability")
            st.metric(label="Chasing Team Win Probability", 
                      value=f"{proba_win * 100:.2f}%",
                      delta=f"{round(proba_win - 0.5, 4) * 200:.2f} Pct. Margin",
                      delta_color="normal")