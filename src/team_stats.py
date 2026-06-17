import pandas as pd

df = pd.read_csv("data/results.csv")
df = df.dropna(subset=["home_score","away_score"])
df["date"] = pd.to_datetime(df["date"])

print(df["date"].head())
df = df.sort_values("date")
print(df[["date","home_team","away_team"]].head())