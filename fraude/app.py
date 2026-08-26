from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
import pandas as pd
import joblib
from fastapi.middleware.cors import CORSMiddleware
# Create FastAPI application
app = FastAPI(
    title="Fraud Detection AI",
    description="Machine Learning API for Fraud Detection",
    version="1.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
import os
import joblib

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model = joblib.load(os.path.join(BASE_DIR, "fraud_detection_pipeline.pkl"))
feature_columns = joblib.load(os.path.join(BASE_DIR, "feature_columns.pkl"))
reference_transaction = joblib.load(os.path.join(BASE_DIR, "reference_transaction.pkl"))

# Home route
@app.get("/")
def home():
    return {
        "message": "Fraud Detection API is running successfully!"
    }


# Health check route
@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


# Prediction route
@app.post("/predict")
def predict(transaction: dict):

    try:
        # Start with a complete transaction containing
        # all features expected by the trained model
        input_data = reference_transaction.copy()

        # Replace only values sent from the website
        for column, value in transaction.items():

            if column in input_data.columns:
                input_data.loc[:, column] = value

        # Keep feature order exactly the same as training
        input_data = input_data[feature_columns]

        # Prediction
        prediction = model.predict(input_data)[0]

        # Fraud probability
        probability = model.predict_proba(input_data)[0][1]

        # Result
        result = "Fraud" if prediction == 1 else "Not Fraud"

        # Risk level
        if probability < 0.30:
            risk_level = "Low"
        elif probability < 0.70:
            risk_level = "Medium"
        else:
            risk_level = "High"

        return {
            "prediction": int(prediction),
            "result": result,
            "fraud_probability": round(float(probability) * 100, 2),
            "risk_level": risk_level
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )