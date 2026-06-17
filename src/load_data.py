import pandas as pd

df = pd.read_csv("data/results.csv")

print(df.head())
print("\nRows, Columns:", df.shape)