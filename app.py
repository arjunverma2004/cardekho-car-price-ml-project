import streamlit as st
import pandas as pd
import joblib

st.markdown(
    """
    <style>
    .reportview-container {
        background: url("sweetwarm-bg-color.png")
    }

    </style>
    """,
    unsafe_allow_html=True
)


# Load models
price_model = joblib.load("models/model.pkl")
preprocessor=joblib.load("models/preprocessor.pkl")
le=joblib.load("models/le.pkl")

def process_input_data(data):
    # Apply label encoding to the 'model' column
    data['model'] = le.transform(data['model'])
    # Preprocess the entire data using the preprocessor
    processed_data = preprocessor.transform(data)
    return processed_data


# Title
st.title("🚗 Used Car Price Predictor & Analyzer")
st.write("Predict the resale price of a used car and check if it is overpriced!")

# Input columns
cols = st.columns(2)

with cols[0].container(height=100):
    model = st.selectbox("Car Model", ['Alto', 'Grand', 'i20', 'Ecosport', 'Wagon R', 'i10', 'Venue',
       'Swift', 'Verna', 'Duster', 'Cooper', 'Ciaz', 'C-Class', 'Innova',
       'Baleno', 'Swift Dzire', 'Vento', 'Creta', 'City', 'Bolero',
       'Fortuner', 'KWID', 'Amaze', 'Santro', 'XUV500', 'KUV100', 'Ignis',
       'RediGO', 'Scorpio', 'Marazzo', 'Aspire', 'Figo', 'Vitara',
       'Tiago', 'Polo', 'Seltos', 'Celerio', 'GO', '5', 'CR-V',
       'Endeavour', 'KUV', 'Jazz', '3', 'A4', 'Tigor', 'Ertiga', 'Safari',
       'Thar', 'Hexa', 'Rover', 'Eeco', 'A6', 'E-Class', 'Q7', 'Z4', '6',
       'XF', 'X5', 'Hector', 'Civic', 'D-Max', 'Cayenne', 'X1', 'Rapid',
       'Freestyle', 'Superb', 'Nexon', 'XUV300', 'Dzire VXI', 'S90',
       'WR-V', 'XL6', 'Triber', 'ES', 'Wrangler', 'Camry', 'Elantra',
       'Yaris', 'GL-Class', '7', 'S-Presso', 'Dzire LXI', 'Aura', 'XC',
       'Ghibli', 'Continental', 'CR', 'Kicks', 'S-Class', 'Tucson',
       'Harrier', 'X3', 'Octavia', 'Compass', 'CLS', 'redi-GO', 'Glanza',
       'Macan', 'X4', 'Dzire ZXI', 'XC90', 'F-PACE', 'A8', 'MUX',
       'GTC4Lusso', 'GLS', 'X-Trail', 'XE', 'XC60', 'Panamera', 'Alturas',
       'Altroz', 'NX', 'Carnival', 'C', 'RX', 'Ghost', 'Quattroporte',
       'Gurkha'])

with cols[1].container(height=100):
    vehicle_age = st.slider("Vehicle Age (Years)", 0, 30, 5)

with cols[0].container(height=100):
    km_driven = st.number_input("Kilometers Driven", min_value=0, value=50000, step=1000)

with cols[1].container(height=100):
    seller_type = st.selectbox("Seller Type", ["Individual", "Dealer", "Trustmark Dealer"])

with cols[0].container(height=100):
    fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG", "LPG", "Electric"])

with cols[1].container(height=100):
    transmission_type = st.selectbox("Transmission", ["Manual", "Automatic"])

with cols[0].container(height=100):
    mileage = st.number_input("Mileage (kmpl)", min_value=0.0, value=18.0, step=0.1)

with cols[1].container(height=100):
    engine = st.number_input("Engine Capacity (CC)", min_value=500, value=1197, step=100)

with cols[0].container(height=100):
    max_power = st.number_input("Max Power (bhp)", min_value=20.0, value=70.0, step=1.0)

with cols[1].container(height=100):
    seats = st.selectbox("Seats", [2, 4, 5, 6, 7, 8, 9])

# Map input to DataFrame
input_data = pd.DataFrame({
    "model": [model],
    "vehicle_age": [vehicle_age],
    "km_driven": [km_driven],
    "seller_type": [seller_type],
    "fuel_type": [fuel_type],
    "transmission_type": [transmission_type],
    "mileage": [mileage],
    "engine": [engine],
    "max_power": [max_power],
    "seats": [seats]
})

# Load encoders/preprocessing (if any)
# Assume preprocess_input is a custom function that matches training pipeline
#from utils import preprocess_input  # This should be implemented separately

if st.button("Predict Price"):
    try:
        processed_data=process_input_data(input_data)


        # Predict price
        predicted_price = price_model.predict(processed_data)[0]

        
        # Output
        st.subheader("🧠 Prediction Result")
        st.success(f"Estimated Resale Price: ₹{predicted_price:,.2f}")
        

    except Exception as e:
        st.error(f"Error during prediction: {e}")
