import numpy as np

def predict_failure_probability(temperature: float, vibration: float, pressure: float) -> float:
    """
    Simple heuristic model that mimics a logistic regression.
    Adjust weights as needed.
    """
    score = (
        0.03 * temperature +
        0.05 * vibration +
        0.02 * pressure -
        5.0
    )
    prob = 1 / (1 + np.exp(-score))
    return float(prob)

def classify_failure(prob: float, threshold: float = 0.6) -> str:
    """
    Convert probability into a binary label.
    """
    return "Will fail soon" if prob >= threshold else "Low risk"