# FIFA World Cup 2026 Match Predictor

### 🇬🇧 England vs 🇭🇷 Croatia

A machine learning project that predicts international football match outcomes using Elo Ratings, recent team form, and XGBoost trained on more than **49,000 historical international matches**.

---

## Overview

This project uses historical international football data to predict the probability of:

* 🇬🇧 England Win
* Draw
* 🇭🇷 Croatia Win

The prediction pipeline combines:

* Elo Ratings
* Recent Form (Last 5 Matches)
* Goal Difference Statistics
* Neutral Venue Information
* Head-to-Head Statistics
* XGBoost Classification

---

## Sample Prediction

### 🇬🇧 England vs 🇭🇷 Croatia

**Competition:** FIFA World Cup 2026

**Venue:** Arlington, Texas, USA 🇺🇸

**Neutral Venue:** Yes

| Outcome          | Probability |
| ---------------- | ----------: |
| 🇬🇧 England Win |      25.00% |
| Draw             |      31.61% |
| 🇭🇷 Croatia Win |      43.39% |

**Predicted Result:** 🇭🇷 Croatia

---

## Dataset

International Football Results Dataset

* 49,425 International Matches
* 336 National Teams
* Coverage from 1872–2026

Dataset Source:

https://github.com/martj42/international_results

---

## Feature Engineering

For every historical match, features are generated using information available before kickoff.

### Elo Features

| Feature      |
| ------------ |
| home_elo     |
| away_elo     |
| elo_diff     |
| abs_elo_diff |

### Form Features

Based on each team's previous 5 matches.

| Feature        |
| -------------- |
| home_win_rate  |
| away_win_rate  |
| home_goal_diff |
| away_goal_diff |

### Match Features

| Feature |
| ------- |
| neutral |

### Head-to-Head Features

| Feature          |
| ---------------- |
| h2h_home_winrate |
| h2h_home_gd      |

---

## Machine Learning Pipeline

```text
Historical Match Results
          │
          ▼
Feature Engineering
          │
          ▼
features.csv
          │
          ▼
XGBoost Training
          │
          ▼
football_model.pkl
          │
          ▼
Future Match Prediction
```

---

## Model

**Algorithm:** XGBoost Classifier

### Prediction Classes

```text
0 → First Team Wins
1 → Draw
2 → Second Team Wins
```

### Training Strategy

* Time-Based Train/Test Split
* Balanced Class Weights
* Multi-Class Classification
* Probability-Based Predictions

---

## Results

| Metric   |  Value |
| -------- | -----: |
| Accuracy | 55.89% |
| Matches  | 49,425 |
| Teams    |    336 |

### Feature Importance

| Rank | Feature        |
| ---- | -------------- |
| 1    | elo_diff       |
| 2    | neutral        |
| 3    | away_goal_diff |
| 4    | home_goal_diff |
| 5    | away_elo       |

### Key Findings

* Elo Difference was the strongest predictor.
* Neutral Venue had significant influence on match outcomes.
* Head-to-Head statistics contributed very little.
* Time-based validation provided realistic future-match evaluation.
* Balanced class weighting improved draw prediction.

---

## Project Structure

```text
fifa-world-cup-with-ml/

├── data/
│   └── results.csv
│
├── src/
│   ├── build_dataset.py
│   ├── build_model.py
│   ├── features.py
│   └── predict_match.py
│
├── features.csv
├── football_model.pkl
└── README.md
```

---

## Running the Project

### Generate Features

```bash
python src/build_dataset.py
```

### Train Model

```bash
python src/build_model.py
```

### Predict a Match

```bash
python src/predict_match.py
```

---

## Example Teams

🇬🇧 England
🇭🇷 Croatia
🇧🇷 Brazil
🇦🇷 Argentina
🇫🇷 France
🇪🇸 Spain
🇩🇪 Germany
🇵🇹 Portugal
🇳🇱 Netherlands
🇧🇪 Belgium
🇯🇵 Japan
🇰🇷 South Korea

---

## Future Improvements

* FIFA Rankings
* Expected Goals (xG)
* Tournament Weighting
* Player Availability Data
* Hyperparameter Optimization
* Probability Calibration

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* XGBoost
* Joblib

---

Built for football analytics, machine learning, and sports prediction.

🇬🇧 🇭🇷 🇧🇷 🇦🇷 🇫🇷 🇪🇸 🇩🇪 🇵🇹
