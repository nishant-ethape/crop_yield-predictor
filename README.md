# 🌾 Crop Yield Predictor

An ML-powered web application that predicts crop yield for Indian farmers 
based on region, season, soil inputs, and weather conditions.

## 🔗 Live Demo
https://cropyield-predictor-aygymgatanbnasbyftuwa3.streamlit.app/

## 📌 Problem Statement
Indian farmers often lack data-driven tools to estimate expected crop yield 
before harvest. This app provides yield predictions to help farmers make 
informed decisions about crop selection and resource allocation.

## 📊 Dataset
- Source: Ministry of Agriculture and Farmers Welfare, Government of India
- Records: 15,000+ entries across 37 crops and 30 Indian states
- Time period: 1997–2021

## 🧠 Models Trained
| Model | R² Score | RMSE |
|-------|----------|------|
| Linear Regression | 72.5% | 5.96 |
| Random Forest | 97.2% | 1.90 |
| XGBoost | 97.3% | 1.87 |

**Final Model: XGBoost (97.3% R²)**

## ⚙️ Features Used
- Crop type, State, Season, Year
- Land area, Annual rainfall
- Fertilizer and pesticide usage

## 🛠️ Tech Stack
- Python, Pandas, NumPy
- Scikit-learn, XGBoost
- Streamlit

## ⚠️ Known Limitations
- State-level rainfall data used instead of district-level seasonal rainfall
- Target encoding on Crop and State may introduce mild data leakage
- Market price advisory module planned for Version 2

## 🚀 Version 2 Roadmap
- District-level seasonal rainfall integration
- Mandi price advisory for optimal selling window
- Leave One Out encoding to fix target leakage
