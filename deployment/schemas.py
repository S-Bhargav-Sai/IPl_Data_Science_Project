# schemas.py

from pydantic import BaseModel
from typing import Literal

# Schema for Pre-Match Prediction (XGBoost V6)
class PreMatchPredictionInput(BaseModel):
    # Features used by the Pre-Match Model (V6)
    hist_win_pct_diff: float      
    form_diff: float              
    venue_bias_delta: float       
    toss_decision: Literal["bat", "field"] 

# Schema for Live Match Prediction (WPA Model)
class LivePredictionInput(BaseModel):
    """Features defining the current state of the 2nd innings."""
    cumulative_runs: float       # Runs scored by the chasing team so far
    current_over: float          # The current completed over number (0-19)
    run_rate: float              # Current run rate of the chasing team
    balls_remaining: int         # Total balls remaining in the inning