import pandas as pd

# ----------------------------------
# LOAD DATA
# ----------------------------------

df = pd.read_csv("data/results.csv")

df = df.dropna(subset=["home_score", "away_score"])

df["date"] = pd.to_datetime(df["date"])

df = df.sort_values("date")

print(df.shape)

# ----------------------------------
# INITIAL ELO RATINGS
# ----------------------------------

ratings = {}

teams = set(df["home_team"]) | set(df["away_team"])

for team in teams:
    ratings[team] = 1500

print("Teams:", len(ratings))

# ----------------------------------
# TEAM HISTORY
# ----------------------------------

team_history = {}
h2h_history = {}

for team in teams:
    team_history[team] = []

# ----------------------------------
# HELPER FUNCTION
# ----------------------------------

def get_form_stats(history):

    if len(history) == 0:
        return 0.5, 0

    last5 = history[-5:]

    wins = sum(match["win"] for match in last5)

    goal_diff = sum(
        match["goal_diff"] for match in last5
    )

    return (
        wins / len(last5),
        goal_diff / len(last5)
    )
 ## h2h stats   
def get_h2h_stats(home, away):

    key = tuple(sorted([home, away]))

    history = h2h_history.get(key, [])

    if len(history) == 0:
        return 0.5, 0

    last5 = history[-5:]

    home_points = 0
    goal_diff = 0

    for h in last5:

        if h["home"] == home:

            if h["result"] == 0:
                home_points += 1

            elif h["result"] == 1:
                home_points += 0.5

            goal_diff += h["goal_diff"]

        else:

            if h["result"] == 2:
                home_points += 1

            elif h["result"] == 1:
                home_points += 0.5

            goal_diff -= h["goal_diff"]

    return (
        home_points / len(last5),
        goal_diff / len(last5)
    )

# ----------------------------------
# DATASET
# ----------------------------------

dataset = []

# ----------------------------------
# MATCH LOOP
# ----------------------------------

for _, match in df.iterrows():

    home = match["home_team"]
    away = match["away_team"]

    # ----------------------------------
    # FEATURES BEFORE MATCH
    # ----------------------------------

    home_elo = ratings[home]
    away_elo = ratings[away]

    home_win_rate, home_goal_diff = get_form_stats(
        team_history[home]
    )

    away_win_rate, away_goal_diff = get_form_stats(
        team_history[away]
    )
    
    h2h_home_winrate, h2h_home_gd = get_h2h_stats(
    home,
    away
    )

    # ----------------------------------
    # TARGET
    # ----------------------------------

    if match["home_score"] > match["away_score"]:
        result = 0

    elif match["home_score"] < match["away_score"]:
        result = 2

    else:
        result = 1

    # ----------------------------------
    # STORE TRAINING ROW
    # ----------------------------------

    dataset.append({
        "home_elo": home_elo,
        "away_elo": away_elo,
        "elo_diff": home_elo - away_elo,
        
        "abs_elo_diff": abs(home_elo - away_elo),

        "home_win_rate": home_win_rate,
        "away_win_rate": away_win_rate,

        "home_goal_diff": home_goal_diff,
        "away_goal_diff": away_goal_diff,
        
        "h2h_home_winrate": h2h_home_winrate,
        "h2h_home_gd": h2h_home_gd,

        "neutral": int(match["neutral"]),

        "result": result
        
    })

    # ----------------------------------
    # ELO UPDATE
    # ----------------------------------

    home_expected = 1 / (
        1 + 10 ** ((away_elo - home_elo) / 400)
    )

    away_expected = 1 / (
        1 + 10 ** ((home_elo - away_elo) / 400)
    )

    if result == 0:
        home_actual = 1
        away_actual = 0

    elif result == 2:
        home_actual = 0
        away_actual = 1

    else:
        home_actual = 0.5
        away_actual = 0.5

    ratings[home] = (
        home_elo +
        20 * (home_actual - home_expected)
    )

    ratings[away] = (
        away_elo +
        20 * (away_actual - away_expected)
    )

    # ----------------------------------
    # UPDATE HISTORY
    # ----------------------------------

    home_gd = (
        match["home_score"]
        - match["away_score"]
    )

    away_gd = (
        match["away_score"]
        - match["home_score"]
    )

    if result == 0:

        team_history[home].append({
            "win": 1,
            "goal_diff": home_gd
        })

        team_history[away].append({
            "win": 0,
            "goal_diff": away_gd
        })

    elif result == 2:

        team_history[home].append({
            "win": 0,
            "goal_diff": home_gd
        })

        team_history[away].append({
            "win": 1,
            "goal_diff": away_gd
        })

    else:

        team_history[home].append({
            "win": 0.5,
            "goal_diff": home_gd
        })

        team_history[away].append({
            "win": 0.5,
            "goal_diff": away_gd
        })
        
        
    key = tuple(sorted([home, away]))

    if key not in h2h_history:
        h2h_history[key] = []

    h2h_history[key].append({
        "home": home,
        "result": result,
        "goal_diff": (
            match["home_score"] - match["away_score"]
        )
    })

# ----------------------------------
# DATAFRAME
# ----------------------------------

features_df = pd.DataFrame(dataset)

print("\nFirst 10 rows:")
print(features_df.head(10))

print("\nShape:")
print(features_df.shape)

print("\nFinal Ratings:")
print("England:", round(ratings["England"], 2))
print("Croatia:", round(ratings["Croatia"], 2))

# ----------------------------------
# SAVE DATASET
# ----------------------------------

features_df.to_csv("features.csv", index=False)

print("\nSaved features.csv")