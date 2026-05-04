import numpy as np

def predict_travel_time(distance):
    # simple linear + noise model
    return 0.6 * distance + np.random.normal(0, 5)

def simulate_delivery_times(distances):
    return [predict_travel_time(d) for d in distances]