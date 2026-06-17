import pandas as pd

# Load data
df = pd.read_csv("data/results.csv")
df = df.dropna(subset=["home_score", "away_score"])

# Convert and sort dates
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

# Initialize ratings
ratings = {}

teams = set(df["home_team"]) | set(df["away_team"])

for team in teams:
    ratings[team] = 1500


# Elo expected score
def expected_score(rating_a, rating_b):
    return 1 / (1 + 10 ** ((rating_b - rating_a) / 400))


# Elo update formula
def update_elo(rating, actual, expected, k=20):
    return rating + k * (actual - expected)


# Process matches
for _, match in df.iterrows():

    home = match["home_team"]
    away = match["away_team"]

    home_rating = ratings[home]
    away_rating = ratings[away]

    # Expected results
    home_expected = expected_score(home_rating, away_rating)
    away_expected = expected_score(away_rating, home_rating)

    # Actual results
    if match["home_score"] > match["away_score"]:
        home_actual = 1
        away_actual = 0

    elif match["home_score"] < match["away_score"]:
        home_actual = 0
        away_actual = 1

    else:
        home_actual = 0.5
        away_actual = 0.5
        
    ratings[home] = update_elo(
      home_rating, home_actual, home_expected
    )

    ratings[away] = update_elo(
      away_rating, away_actual, away_expected
    )

print("Loop finished")
print("England:", round(ratings["England"], 2))
print("Croatia:", round(ratings["Croatia"], 2))
print("Brazil:", round(ratings["Brazil"], 2))
print("Argentina:", round(ratings["Argentina"], 2))