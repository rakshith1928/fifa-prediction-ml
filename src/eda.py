import pandas as pd

df = pd.read_csv("data/results.csv")

print(df.info())

print(df.isnull().sum())