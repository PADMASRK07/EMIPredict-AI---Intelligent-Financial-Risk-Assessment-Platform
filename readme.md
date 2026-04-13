# EMIPredict AI - Intelligent Financial Risk Assessment Platform

## Overview
EMIPredict AI is a FinTech-based machine learning platform designed to assess financial risk and predict EMI eligibility and affordability. It combines classification and regression models with MLflow tracking and a Streamlit web app for real-time insights.

## Key Features
- EMI Eligibility Prediction (Classification)
- Maximum EMI Amount Prediction (Regression)
- MLflow Experiment Tracking & Model Registry
- Advanced Feature Engineering (22 variables)
- Real-time Predictions via Streamlit App
- CRUD Operations for Financial Data
- Cloud Deployment on Streamlit

## Tech Stack
- Python
- Machine Learning (Scikit-learn, XGBoost)
- MLflow
- Streamlit
- Pandas, NumPy, Matplotlib, Seaborn

## Dataset
- 400,000 financial records
- 22 input features (demographics, income, expenses, credit data)
- 2 targets:
  - `emi_eligibility` (Eligible, High Risk, Not Eligible)
  - `max_monthly_emi` (₹500 – ₹50,000)

## ML Approach
- **Classification Models:** Logistic Regression, Random Forest, XGBoost
- **Regression Models:** Linear Regression, Random Forest, XGBoost
- Model evaluation using standard metrics (Accuracy, F1, RMSE, R²)
- Best models selected via MLflow tracking

## Application
- Multi-page Streamlit app
- Real-time EMI predictions
- Interactive dashboards & model monitoring

## Business Impact
- Automates loan approval process
- Improves financial risk assessment
- Enables data-driven lending decisions

## Deployment
- Hosted on Streamlit Cloud
- Integrated with GitHub for CI/CD