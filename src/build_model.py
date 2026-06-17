import pandas as pd
import joblib

from sklearn.utils.class_weight import compute_sample_weight
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

from xgboost import XGBClassifier

# -------------------------
# LOAD DATASET
# -------------------------

df = pd.read_csv("features.csv")

print("Dataset Shape:")
print(df.shape)

# -------------------------
# TARGET DISTRIBUTION
# -------------------------

print("\nTarget Distribution:")
print(df["result"].value_counts())

print("\nTarget Distribution (%):")
print(
    df["result"]
    .value_counts(normalize=True)
    .sort_index()
)

# -------------------------
# FEATURES AND TARGET
# -------------------------

X = df.drop("result", axis=1)

y = df["result"]

print("\nFeature Columns:")
print(list(X.columns))

# -------------------------
# TRAIN TEST SPLIT
# -------------------------

# -------------------------
# TIME-BASED SPLIT
# -------------------------

split_idx = int(len(df) * 0.8)

train_df = df.iloc[:split_idx]
test_df = df.iloc[split_idx:]

X_train = train_df.drop("result", axis=1)
y_train = train_df["result"]

X_test = test_df.drop("result", axis=1)
y_test = test_df["result"]

print("\nTrain Size:", len(X_train))
print("Test Size:", len(X_test))

# -------------------------
# MODEL
# -------------------------

model = XGBClassifier(
    objective="multi:softprob",
    num_class=3,

    n_estimators=200,
    max_depth=5,
    learning_rate=0.05,

    random_state=42
)

# -------------------------
# TRAIN
# -------------------------

weights = compute_sample_weight(
    class_weight="balanced",
    y=y_train
)
print("\nTraining Model...")

model.fit(X_train, y_train, sample_weight=weights)

print("Training Complete!")

# -------------------------
# SAVE MODEL
# -------------------------

joblib.dump(
    model,
    "football_model.pkl"
)

print("Model Saved: football_model.pkl")

# -------------------------
# PREDICT
# -------------------------

preds = model.predict(X_test)

# -------------------------
# EVALUATION
# -------------------------

accuracy = accuracy_score(
    y_test,
    preds
)

print("\nAccuracy:")
print(round(accuracy, 4))

print("\nClassification Report:")
print(
    classification_report(
        y_test,
        preds
    )
)

# -------------------------
# FEATURE IMPORTANCE
# -------------------------

importance = pd.DataFrame({
    "feature": X.columns,
    "importance": model.feature_importances_
})

importance = importance.sort_values(
    by="importance",
    ascending=False
)

print("\nFeature Importance:")
print(importance)

# -------------------------
# TOP 5 FEATURES
# -------------------------

print("\nTop 5 Features:")
print(importance.head())


