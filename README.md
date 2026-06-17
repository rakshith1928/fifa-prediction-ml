# 🌍 FIFA World Cup 2026 ⚽ Match Predictor

Predicting the **England vs Croatia** World Cup clash using machine learning trained on 49,000+ historical international matches.

---

## Table of Contents

- [Overview](#overview)
- [Dataset](#dataset)
- [Feature Engineering](#feature-engineering)
- [Model](#model)
- [Results](#results)
- [England vs Croatia](#england-vs-croatia)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)
- [Technologies Used](#technologies-used)

---

## Overview

This project applies **XGBoost classification** to predict the outcome of England vs Croatia at the FIFA World Cup 2026 ⚽. It engineers features from over a century of international match data, including Elo ratings, team form, and head-to-head statistics, then trains a multi-class classifier to output win/draw/loss probabilities for any given matchup.

The pipeline is deliberately time-aware: features are computed using only information available before each match, and the train/test split respects chronological order to simulate real-world prediction.

---

## Dataset

The dataset is sourced from [martj42/international_results](https://github.com/martj42/international_results).

| Statistic | Value |
|-----------|-------|
| Total Matches | 49,425 |
| National Teams | 336 |
| Date Range | 1872 - 2026 |
| Source License | MIT |

The raw data is stored in `data/results.csv` and contains columns for date, home team, away team, home score, away score, tournament, and neutral venue flag.

---

## Feature Engineering

For each match, features are constructed using only data available before kickoff.

### Elo Ratings

| Feature | Description |
|---------|-------------|
| `home_elo` | Home team Elo rating before the match |
| `away_elo` | Away team Elo rating before the match |
| `elo_diff` | Difference in Elo ratings |
| `abs_elo_diff` | Absolute Elo difference |

Elo ratings are initialized at 1500 and updated after each match with K=20 using the standard Elo formula.

### Team Form

Computed from each team's last 5 matches.

| Feature | Description |
|---------|-------------|
| `home_win_rate` | Home team win rate in last 5 matches |
| `away_win_rate` | Away team win rate in last 5 matches |
| `home_goal_diff` | Home team average goal difference in last 5 |
| `away_goal_diff` | Away team average goal difference in last 5 |

### Match Context

| Feature | Description |
|---------|-------------|
| `neutral` | Whether the match is at a neutral venue (1) or not (0) |

### Head-to-Head

| Feature | Description |
|---------|-------------|
| `h2h_home_winrate` | Home team win rate in last 5 meetings |
| `h2h_home_gd` | Home team average goal difference in last 5 meetings |

---

## Model

**Algorithm:** XGBoost Classifier ⚙️ (`multi:softprob` objective)

**Prediction Classes:**

| Class | Meaning |
|-------|---------|
| 0 | First team wins |
| 1 | Draw |
| 2 | Second team wins |

**Training Configuration:**

| Parameter | Value |
|-----------|-------|
| Estimators | 200 |
| Max Depth | 5 |
| Learning Rate | 0.05 |
| Split | Time-based 80/20 |
| Class Weights | Balanced (sample_weight) |

---

## Results

### Accuracy

| Metric | Value |
|--------|-------|
| Test Accuracy | 55.89% |
| Training Matches | 39,540 |
| Test Matches | 9,885 |
| Total Teams | 336 |

### Feature Importance

| Rank | Feature | Contribution |
|------|---------|-------------|
| 1 | `elo_diff` | Highest predictive power |
| 2 | `neutral` | Strong venue influence |
| 3 | `away_goal_diff` | Significant form indicator |
| 4 | `home_goal_diff` | Significant form indicator |
| 5 | `away_elo` | Team strength proxy |

### Key Findings

- Elo difference is the single strongest predictor of match outcome.
- Neutral venue signficantly affects prediction (relevant for World Cup matches).
- Head-to-head statistics contribute minimally compared to broader form and Elo.
- Time-based validation ensures no data leakage from future matches into training.
- Balanced class weighting improves recall for the draw class.

---

## England vs Croatia

This project centers on the upcoming **FIFA World Cup 2026** match between **England and Croatia**, a rivalry renewed since their iconic 2018 World Cup semi-final in Moscow where Croatia won 2-1 in extra time.

### Sample Prediction

| Outcome | Probability |
|---------|-----------:|
| England Win | 25.00% |
| Draw | 31.61% |
| Croatia Win | 43.39% |

**Predicted Result:** Croatia Win 🏆

**Match Details:**

- Competition: FIFA World Cup 2026 🌍
- Venue: Arlington, Texas, USA
- Neutral Venue: Yes

### Historical Context

- 2018 World Cup Semi-Final: Croatia 2-1 England (AET)
- 2020 UEFA Nations League: England 2-1 Croatia, Croatia 1-0 England
- The teams have faced each other 11 times since their first meeting in 1996.
- The rivalry spans the World Cup, UEFA Nations League, and European Championship qualifiers.

---

## Project Structure

```
fifa-world-cup-with-ml/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   └── feature_request.md
│   └── pull_request_template.md
├── assets/
│   └── README.md
├── data/
│   └── results.csv
├── src/
│   ├── build_dataset.py        # Feature engineering pipeline
│   ├── build_model.py          # Model training and evaluation
│   ├── features.py             # Elo and form computation
│   └── predict_match.py        # Match prediction script
├── .editorconfig
├── .gitignore
├── CHANGELOG.md
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE
├── README.md
└── requirements.txt
```

---

## Usage

### Prerequisites

- Python 3.13+
- Virtual environment (recommended)

### Installation

```bash
git clone https://github.com/yourusername/fifa-world-cup-with-ml.git
cd fifa-world-cup-with-ml
python -m venv .venv
.venv\Scripts\activate       # Windows
# source .venv/bin/activate  # macOS/Linux
pip install -r requirements.txt
```

### Pipeline

```bash
# Step 1: Build feature dataset
python src/build_dataset.py

# Step 2: Train the model
python src/build_model.py

# Step 3: Predict a match
python src/predict_match.py
```

To predict a different match, edit the team names in `src/predict_match.py`:

```python
home_team = "Brazil"
away_team = "Argentina"
```

---

## Future Improvements

- Integrate FIFA World Rankings alongside Elo
- Add expected goals (xG) data for advanced form metrics
- Weight recent matches and tournament matches more heavily
- Incorporate player availability and injury data
- Hyperparameter optimization via grid search
- Probability calibration for sharper predictions
- Ensemble methods combining XGBoost with Random Forest and LightGBM
- Web interface for interactive match predictions

---

## Contributing

Contributions are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on:

- Adding new match predictions
- Improving the model with additional features
- Enhancing the feature engineering pipeline
- Bug fixes and documentation

---

## Technologies Used

| Tool | Purpose |
|------|---------|
| Python 3.13 | Core programming language |
| Pandas | Data processing and feature engineering |
| XGBoost | Gradient boosting classification |
| Scikit-learn | Train/test split, evaluation metrics, class weighting |
| Joblib | Model serialization |

---

## License

This project is open source under the MIT License. See [LICENSE](LICENSE).

---

Built for sports analytics, machine learning, and the beautiful game. ⚽
