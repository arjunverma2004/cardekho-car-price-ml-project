import pandas as pd
import joblib


preprocessor=joblib.load("models/preprocessor.pkl")
le=joblib.load("models/le.pkl") 
df=pd.read_csv('data/cardekho_imputated.csv')


def process_input_data(data):
    # Apply label encoding to the 'model' column
    data['model'] = le.transform(data['model'])
    # Preprocess the entire data using the preprocessor
    processed_data = preprocessor.transform(data)
    return processed_data

class selectbox_values():
  def __init__(self, model):
     self.car_model=model
  def fuel_type(self):
    fuel_type=df.loc[df['model'] == self.car_model]['fuel_type'].unique()
    return fuel_type
  def transmission_type(self):
    transmission_type=df.loc[df['model'] == self.car_model]['transmission_type'].unique()
    return transmission_type
  def seats(self):
    seats=df.loc[df['model'] == self.car_model]['seats'].unique()
    return seats
  def engine(self):
    engine=df.loc[df['model'] == self.car_model]['engine'].median()
    return engine
  def engine(self):
    engine=df.loc[df['model'] == self.car_model]['engine'].unique()
    return engine
  def km_driven(self):
    km_driven=df.loc[df['model'] == self.car_model]['km_driven'].median()
    return int(km_driven)
  def max_power(self):
    max_power=df.loc[df['model'] == self.car_model]['max_power'].median()
    return int(max_power)
  def mileage(self):
    mileage=df.loc[df['model'] == self.car_model]['mileage'].median()
    return float(mileage)