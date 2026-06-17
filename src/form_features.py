import pandas as pd

df = pd.read_csv("data/results.csv")
df = df.dropna(subset=["home_score", "away_score"])

df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

team = "England"

matches = df[
    (df["home_team"] == team) |
    (df["away_team"] == team)
]

print(matches.tail(5)[[
    "date",
    "home_team",
    "away_team",
    "home_score",
    "away_score"
]])

last5 = matches.tail(5)

wins = 0

for _, match in last5.iterrows():

    if match["home_team"] == team:

        if match["home_score"] > match["away_score"]:
            wins += 1

    else:

        if match["away_score"] > match["home_score"]:
            wins += 1

print("Wins:", wins)
print("Win Rate:", wins / len(last5))

goal_diff = 0

for _, match in last5.iterrows():

    if match["home_team"] == team:
        goal_diff += (
            match["home_score"] - match["away_score"]
        )
    else:
        goal_diff += (
            match["away_score"] - match["home_score"]
        )

print("Avg Goal Diff:", goal_diff / len(last5))