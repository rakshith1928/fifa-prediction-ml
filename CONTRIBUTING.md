# Contributing

Contributions are welcome! Whether it's improving the model, adding new matches, or enhancing the pipeline — here's how to get started.

## Ideas for Contributions

- Add new match predictions (France vs Argentina, Brazil vs Germany, etc.)
- Improve model accuracy with better features
- Add visualizations and charts
- Enhance ELO rating calculations
- Add cross-validation for better evaluation
- Create a web interface for predictions
- Add more historical data sources

## Setup

```bash
git clone https://github.com/yourusername/fifa-world-cup-with-ml.git
cd fifa-world-cup-with-ml
python -m venv .venv
.venv\Scripts\activate       # Windows
# source .venv/bin/activate  # macOS/Linux
pip install -r requirements.txt
```

## How to Contribute

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Test your changes (`python src/predict_match.py`)
5. Commit (`git commit -m 'Add amazing feature'`)
6. Push (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## Adding a New Match Prediction

1. Open `src/predict_match.py`
2. Update the team names:

```python
home_team = "Your Home Team"
away_team = "Your Away Team"
```

3. Run the prediction:

```bash
python src/predict_match.py
```

## Improving the Model

- Experiment with different algorithms (Random Forest, LightGBM, Neural Networks)
- Add new features (player ratings, recent tournament performance, home advantage)
- Tune hyperparameters
- Add ensemble methods

## Code Style

- Follow PEP 8
- Use meaningful variable names
- Add comments for complex logic
- Keep functions focused

## Questions?

Open an issue or start a discussion. Let's predict the beautiful game together!
