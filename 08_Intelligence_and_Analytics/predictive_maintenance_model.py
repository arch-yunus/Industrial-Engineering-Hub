"""
Predictive Maintenance Basic Simulation Model
"""
def predict_time_to_failure(current_wear, wear_rate, failure_threshold):
    """
    Predicts remaining useful life (RUL) under a linear degradation model.
    """
    if current_wear >= failure_threshold:
         return 0
    rul = (failure_threshold - current_wear) / wear_rate
    return round(rul, 2)

if __name__ == "__main__":
    rul = predict_time_to_failure(current_wear=30, wear_rate=2.5, failure_threshold=100)
    print(f"Remaining Useful Life Predictor: {rul} periods before maintenance required.")
