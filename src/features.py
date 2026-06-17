import pandas as pd

# -----------------------------
# LOAD DATA
# -----------------------------

df = pd.read_csv("data/results.csv")

df = df.dropna(subset=["home_score", "away_score"])

df["date"] = pd.to_datetime(df["date"])

df = df.sort_values("date")


# -----------------------------
# ELO FUNCTIONS
# -----------------------------

def expected_score(rating_a, rating_b):
    return 1 / (1 + 10 ** ((rating_b - rating_a) / 400))


def update_elo(rating, actual, expected, k=20):
    return rating + k * (actual - expected)


# -----------------------------
# BUILD ELO RATINGS
# -----------------------------

ratings = {}

teams = set(df["home_team"]) | set(df["away_team"])

for team in teams:
    ratings[team] = 1500


for _, match in df.iterrows():

    home = match["home_team"]
    away = match["away_team"]

    home_rating = ratings[home]
    away_rating = ratings[away]

    home_expected = expected_score(
        home_rating,
        away_rating
    )

    away_expected = expected_score(
        away_rating,
        home_rating
    )

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
        home_rating,
        home_actual,
        home_expected
    )

    ratings[away] = update_elo(
        away_rating,
        away_actual,
        away_expected
    )


# -----------------------------
# LAST 5 FORM FEATURES
# -----------------------------

def get_last5_stats(team):

    matches = df[
        (df["home_team"] == team)
        | (df["away_team"] == team)
    ]

    last5 = matches.tail(5)

    wins = 0
    goal_diff = 0

    for _, match in last5.iterrows():

        if match["home_team"] == team:

            if match["home_score"] > match["away_score"]:
                wins += 1

            goal_diff += (
                match["home_score"]
                - match["away_score"]
            )

        else:

            if match["away_score"] > match["home_score"]:
                wins += 1

            goal_diff += (
                match["away_score"]
                - match["home_score"]
            )

    return {
        "win_rate": wins / len(last5),
        "goal_diff": goal_diff / len(last5)
    }


# -----------------------------
# TEAM FEATURE FUNCTION
# -----------------------------

def get_team_features(team):

    form = get_last5_stats(team)

    return {
        "elo": round(ratings[team], 2),
        "win_rate": round(form["win_rate"], 2),
        "goal_diff": round(form["goal_diff"], 2)
    }

