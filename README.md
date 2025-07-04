# 🚗 CarDekho Car Price Prediction - ML App

This is a machine learning web app that predicts the selling price of a used car based on key input features. The model is trained on the CarDekho dataset and deployed using **Streamlit**.

🔗 **Live App:** [Car Price Prediction App](https://cardekho-car-price-ml-project-zhxu3enk8syswiacwye8ip.streamlit.app/)

---

## 📊 Features

- Predict used car prices based on inputs like:
  - Year of purchase
  - Present price
  - Kms driven
  - Fuel type
  - Seller type
  - Transmission type
  - Number of previous owners
- Intuitive and easy-to-use interface via Streamlit
- Model trained using regression algorithms (Random Forest/Linear Regression)
- Scikit-learn based pipeline

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Pandas, NumPy
- Scikit-learn
- Joblib (for model serialization)

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone github.com/arjunverma2004/cardekho-car-price-ml-project.git
cd cardekho-car-price-prediction
```

### 2. Create a Virtual Environment (Optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate     # For Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the App Locally
```bash
streamlit run app.py
```

