<div align="center">

# 🌍 FIFA World Cup 2026 ⚽ Match Predictor

**England vs Croatia** — predicted by machine learning trained on 49,000+ historical matches.

![Python](https://img.shields.io/badge/Python-3.13-3776AB?logo=python&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-2.0-FF6F00?logo=xgboost&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=white)
![Scikit--learn](https://img.shields.io/badge/Scikit--learn-F7931E?logo=scikit-learn&logoColor=white)
![Acccuracy](https://img.shields.io/badge/Accuracy-55.89%25-success)
![License](https://img.shields.io/badge/License-MIT-blue)
![Matches](https://img.shields.io/badge/Matches-49,425-blueviolet)

---

</div>

## 📋 Table of Contents

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

## 📖 Overview

This project applies **XGBoost classification** to predict the outcome of England vs Croatia at the FIFA World Cup 2026 ⚽. It engineers features from over a century of international match data, including Elo ratings, team form, and head-to-head statistics, then trains a multi-class classifier to output win/draw/loss probabilities for any given matchup.

The pipeline is deliberately time-aware: features are computed using only information available before each match, and the train/test split respects chronological order to simulate real-world prediction.

```
┌─────────────────┐     ┌──────────────────┐     ┌──────────────┐     ┌──────────────────┐
│ Historical Data │ ──▶ │ Feature Pipeline │ ──▶ │ XGBoost      │ ──▶ │ Match Prediction  │
│  (1872–2026)    │     │ (Elo, Form, H2H) │     │ Training     │     │ (Win/Draw/Loss %) │
└─────────────────┘     └──────────────────┘     └──────────────┘     └──────────────────┘
```

---

## 📊 Dataset

The dataset is sourced from [martj42/international_results](https://github.com/martj42/international_results).

<div align="center">

| 📈 Statistic | 🔢 Value |
|:------------:|:--------:|
| Total Matches | 49,425 |
| National Teams | 336 |
| Date Range | 1872 – 2026 |
| Source License | MIT |

</div>

The raw data is stored in `data/results.csv` with columns for date, home team, away team, home score, away score, tournament, and neutral venue flag.

---

## 🔧 Feature Engineering

For each match, features are constructed using only data available before kickoff.

### ⭐ Elo Ratings

| Feature | Description |
|---------|-------------|
| `home_elo` | Home team Elo rating before the match |
| `away_elo` | Away team Elo rating before the match |
| `elo_diff` | Difference in Elo ratings |
| `abs_elo_diff` | Absolute Elo difference |

Elo ratings are initialized at **1500** and updated after each match with **K=20** using the standard Elo formula.

### 📈 Team Form

Computed from each team's last **5 matches**.

| Feature | Description |
|---------|-------------|
| `home_win_rate` | Home team win rate in last 5 matches |
| `away_win_rate` | Away team win rate in last 5 matches |
| `home_goal_diff` | Home team average goal difference in last 5 |
| `away_goal_diff` | Away team average goal difference in last 5 |

### 🏟️ Match Context

| Feature | Description |
|---------|-------------|
| `neutral` | Neutral venue (1) or not (0) |

### 🤝 Head-to-Head

| Feature | Description |
|---------|-------------|
| `h2h_home_winrate` | Home team win rate in last 5 meetings |
| `h2h_home_gd` | Home team average goal difference in last 5 meetings |

---

## 🤖 Model

<div align="center">

**Algorithm:** XGBoost Classifier ⚙️ (`multi:softprob` objective)

</div>

### 🎯 Prediction Classes

| Class | Meaning |
|:-----:|---------|
| 0 | First team wins |
| 1 | Draw |
| 2 | Second team wins |

### ⚙️ Training Configuration

| Parameter | Value |
|-----------|-------|
| Estimators | 200 |
| Max Depth | 5 |
| Learning Rate | 0.05 |
| Split | Time-based 80/20 |
| Class Weights | Balanced (`sample_weight`) |

---

## 📈 Results

### 🎯 Accuracy

<div align="center">

| Metric | Value |
|:------:|:-----:|
| Test Accuracy | **55.89%** |
| Training Matches | 39,540 |
| Test Matches | 9,885 |
| Total Teams | 336 |

</div>

### 🔑 Feature Importance

| Rank | Feature | Contribution |
|:----:|---------|:------------:|
| 🥇 1 | `elo_diff` | Highest predictive power |
| 🥈 2 | `neutral` | Strong venue influence |
| 🥉 3 | `away_goal_diff` | Significant form indicator |
| 4 | `home_goal_diff` | Significant form indicator |
| 5 | `away_elo` | Team strength proxy |

### 📝 Key Findings

- ✅ **Elo difference** is the single strongest predictor of match outcome.
- ✅ **Neutral venue** significantly affects prediction (critical for World Cup).
- ✅ **Head-to-head** contributes minimally compared to broader form and Elo.
- ✅ **Time-based validation** ensures no data leakage from future matches.
- ✅ **Balanced class weighting** improves recall for the draw class.

---

## ⚔️ England vs Croatia

This project centers on the upcoming **FIFA World Cup 2026** match between **England and Croatia**, a rivalry renewed since their iconic **2018 World Cup semi-final** in Moscow where Croatia won 2-1 in extra time.

### 🎲 Sample Prediction

<div align="center">

| Outcome | Probability |
|:-------:|:-----------:|
| England Win | 25.00% |
| Draw | 31.61% |
| Croatia Win | **43.39%** |

**Predicted Result:** Croatia Win 🏆

</div>

### 📋 Match Details

| Detail | Info |
|--------|------|
| 🏆 Competition | FIFA World Cup 2026 🌍 |
| 📍 Venue | Arlington, Texas, USA |
| 🏟️ Neutral Venue | Yes |

### 📜 Historical Context

| Year | Competition | Result |
|:----:|:-----------:|:------:|
| 2018 | World Cup Semi-Final | Croatia 2-1 England (AET) |
| 2020 | UEFA Nations League | England 2-1 Croatia |
| 2020 | UEFA Nations League | Croatia 1-0 England |

- The teams have faced each other **11 times** since their first meeting in 1996.
- The rivalry spans the World Cup, UEFA Nations League, and European Championship qualifiers.

---

## 📁 Project Structure

```
fifa-world-cup-with-ml/
├── .github/
│   ├── ISSUE_TEMPLATE/          # Bug report & feature request templates
│   └── pull_request_template.md
├── assets/
│   └── README.md                # Screenshot placeholder
├── data/
│   └── results.csv              # 49,425 international match results
├── src/
│   ├── build_dataset.py         # Feature engineering pipeline
│   ├── build_model.py           # Model training & evaluation
│   ├── features.py              # Elo & form computation
│   └── predict_match.py         # Match prediction script
├── .editorconfig
├── .gitignore
├── CHANGELOG.md
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md              # How to contribute / add new matches
├── LICENSE                      # MIT License
├── README.md
└── requirements.txt
```

---

## 🚀 Usage

### Prerequisites

- **Python 3.13+**
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
# Step 1: Build the feature dataset
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

## 🔮 Future Improvements

- [ ] 🌐 Integrate **FIFA World Rankings** alongside Elo
- [ ] ⚡ Add **expected goals (xG)** data for advanced form metrics
- [ ] 🏆 Weight recent matches and **tournament matches** more heavily
- [ ] 🏥 Incorporate **player availability and injury data**
- [ ] 🔬 **Hyperparameter optimization** via grid search
- [ ] 📊 **Probability calibration** for sharper predictions
- [ ] 🧠 **Ensemble methods** combining XGBoost with Random Forest and LightGBM
- [ ] 🌐 **Web interface** for interactive match predictions

---

## 🤝 Contributing

Contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for full guidelines:

- ➕ Adding new match predictions
- 🧠 Improving the model with additional features
- 🔧 Enhancing the feature engineering pipeline
- 🐛 Bug fixes and documentation

---

## 🛠️ Technologies Used

| Tool | Purpose |
|:----:|---------|
| 🐍 **Python 3.13** | Core programming language |
| 🐼 **Pandas** | Data processing and feature engineering |
| ⚡ **XGBoost** | Gradient boosting classification |
| 🔬 **Scikit-learn** | Train/test split, evaluation, class weighting |
| 💾 **Joblib** | Model serialization |

---

## 📄 License

This project is open source under the **MIT License**. See [LICENSE](LICENSE).

---

<div align="center">

**Built with ❤️ for sports analytics, machine learning, and the beautiful game** ⚽

</div>
