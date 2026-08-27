# Credit Card Fraud Detection System

## 🚀 Live Demo

**Frontend Application:**
https://credit-card-fraud-detection-frontend.onrender.com

**Backend API:**
https://credit-card-fraud-detection-8-ayxm.onrender.com

> Update the frontend link above if your deployed frontend has a different Render URL.

---

## 📌 Project Overview

The Credit Card Fraud Detection System is an end-to-end Machine Learning web application designed to analyze credit card transactions and predict whether a transaction is likely to be fraudulent.

The project combines a trained Machine Learning model with a FastAPI backend and an interactive frontend. Users can enter transaction details, and the system sends the data to the backend API for fraud prediction.

---

## ✨ Features

* 🤖 Machine Learning-based fraud detection
* 📊 Transaction risk analysis
* ⚡ FastAPI backend API
* 🌐 Interactive web frontend
* 🔗 Frontend connected to deployed backend
* 🚀 Deployed using Render
* 📦 Pre-trained fraud detection model
* 🎯 Fraud probability prediction
* ⚠️ Risk level classification

---

## 🏗️ Project Architecture

```text
User
  │
  ▼
Frontend Website
  │
  │ Transaction Data
  ▼
FastAPI Backend
  │
  ▼
Data Preprocessing
  │
  ▼
Trained Machine Learning Model
  │
  ├── Fraud Prediction
  ├── Fraud Probability
  └── Risk Level
  │
  ▼
Result Displayed to User
```

---

## 🛠️ Technologies Used

### Machine Learning & Data Science

* Python
* Pandas
* NumPy
* Scikit-learn
* Joblib

### Backend

* FastAPI
* Uvicorn

### Frontend

* HTML
* CSS
* JavaScript

### Deployment

* Render
* GitHub

---

## 📂 Project Structure

```text
credit-card-fraud-detection/
│
├── data/
│   ├── sample_transaction.csv
│   ├── test_identity.csv
│   ├── test_transaction.csv
│   ├── train_identity.csv
│   ├── train_merged.csv
│   └── train_transaction.csv
│
├── fraud/
│   ├── fraud_detection_pipeline.pkl
│   └── reference_transaction.pkl
│
├── frontend/
│   ├── index.html
│   ├── script.js
│   └── style.css
│
├── notebook/
│   ├── creditpre.ipynb
│   └── feature_columns.pkl
│
├── app.py
├── mergecsv.py
├── requirements.txt
├── sample_transaction.json
└── .gitignore
```

---

## 🔄 How the System Works

1. The user enters transaction information on the website.
2. JavaScript collects the transaction data.
3. The frontend sends a `POST` request to the FastAPI backend.
4. The backend receives the transaction data through the `/predict` endpoint.
5. Missing features are handled using the reference transaction data.
6. The features are arranged in the same order used during model training.
7. The trained fraud detection model analyzes the transaction.
8. The system calculates the fraud probability.
9. A risk level is generated.
10. The prediction result is returned and displayed on the frontend.

---

## 🔌 API Endpoint

### Health Check

```text
GET /
```

Example response:

```json
{
  "status": "healthy"
}
```

### Fraud Prediction

```text
POST /predict
```

The API receives transaction data in JSON format and returns a fraud prediction, probability, and risk analysis.

---

## 💻 Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/mdhaseebulhaq/credit-card-fraud-detection.git
```

### 2. Move into the Project Folder

```bash
cd credit-card-fraud-detection
```

### 3. Create a Virtual Environment

```bash
python -m venv creditvenv
```

### 4. Activate the Virtual Environment

Windows:

```bash
creditvenv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the FastAPI Backend

```bash
uvicorn app:app --reload
```

The backend will run locally at:

```text
http://127.0.0.1:8000
```

---

## 🌐 Deployment

The application is deployed using Render.

The frontend communicates with the deployed FastAPI backend:

```text
Frontend
    ↓
POST /predict
    ↓
FastAPI Backend
    ↓
Fraud Detection Model
    ↓
Prediction Result
```

---

## 📊 Example Prediction Output

```json
{
  "prediction": "Not Fraud",
  "fraud_probability": 0.18,
  "risk_level": "Low"
}
```

> The exact output depends on the transaction data and trained model.

---

## 🎯 Key Learning Outcomes

Through this project, I gained practical experience in:

* Data preprocessing
* Feature engineering
* Handling missing features
* Machine Learning model training
* Model serialization using Joblib
* Building REST APIs with FastAPI
* Connecting a frontend with a backend API
* JSON data handling
* API error handling
* Deploying ML applications on Render
* Using Git and GitHub for version control

---

## 👨‍💻 Author

**Md Haseeb Ul Haq**

Aspiring Data Scientist | Machine Learning Enthusiast

GitHub: https://github.com/mdhaseebulhaq

---

## ⭐ Future Improvements

* Add user authentication
* Store transaction history in a database
* Add real-time fraud monitoring
* Create transaction analytics dashboards
* Improve model performance
* Add model explainability
* Add more detailed risk analysis
* Deploy frontend and backend using a custom domain
