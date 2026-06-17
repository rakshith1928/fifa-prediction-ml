import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

import pandas as pd
import joblib

from features import get_team_features

# -------------------------
# LOAD MODEL
# -------------------------

model = joblib.load(
    "football_model.pkl"
)
print("Class Order:")
print(model.classes_)

# -------------------------
# MATCH
# -------------------------

home_team = "England"
away_team = "Croatia"

# -------------------------
# GET TEAM FEATURES
# -------------------------

home = get_team_features(
    home_team
)

away = get_team_features(
    away_team
)

print("\nHome Team Features:")
print(home)

print("\nAway Team Features:")
print(away)

# -------------------------
# BUILD MATCH FEATURES
# -------------------------

match_df = pd.DataFrame([{
    "home_elo": home["elo"],
    "away_elo": away["elo"],

    "elo_diff":
        home["elo"] - away["elo"],
        
    "abs_elo_diff":
        abs(home["elo"] - away["elo"]),

    "home_win_rate":
        home["win_rate"],

    "away_win_rate":
        away["win_rate"],

    "home_goal_diff":
        home["goal_diff"],

    "away_goal_diff":
        away["goal_diff"],

    # Model learned these are useless,
    # but they must exist because
    # the model was trained on them
    "h2h_home_winrate": 0.5,
    "h2h_home_gd": 0,

    # World Cup in USA
    "neutral": 1
}])

print("\nMatch Features:")
print(match_df.T)

# -------------------------
# PREDICT
# -------------------------

probs = model.predict_proba(
    match_df
)[0]

home_win = probs[0]
draw = probs[1]
away_win = probs[2]

print("\nRaw Probabilities:")
print(probs)

# -------------------------
# OUTPUT
# -------------------------

print("\n" + "=" * 40)
print(f"{home_team} vs {away_team}")
print("=" * 40)

print(
    f"\n{home_team} Win : "
    f"{home_win * 100:.2f}%"
)

print(
    f"Draw : "
    f"{draw * 100:.2f}%"
)

print(
    f"{away_team} Win : "
    f"{away_win * 100:.2f}%"
)

classes = [
    home_team,
    "Draw",
    away_team
]

prediction = classes[
    probs.argmax()
]

print("\nPrediction:")
print(prediction)