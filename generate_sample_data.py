# generate_sample_data.py
import pandas as pd
import numpy as np

def generate_sample_dataframe():
    sample_data = {
        'v4': [None] * 31, 'v3': [None] * 31,
        'v2': [None] * 31, 'v1': [None] * 31,
    }
    df_sample = pd.DataFrame(sample_data, index=range(1, 32))
    np.random.seed(42)  # For reproducibility
    for _ in range(20):
        day = np.random.randint(1, 32)
        room = np.random.choice(['v4', 'v3', 'v2', 'v1'])
        event_name = f"Event {_ + 1}"
        df_sample.at[day, room] = event_name
    return df_sample
