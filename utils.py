import pandas as pd
import joblib


preprocessor=joblib.load("models/preprocessor.pkl")
le=joblib.load("models/le.pkl") 


def process_input_data(data):
    # Apply label encoding to the 'model' column
    data['model'] = le.transform(data['model'])
    # Preprocess the entire data using the preprocessor
    processed_data = preprocessor.transform(data)
    return processed_data