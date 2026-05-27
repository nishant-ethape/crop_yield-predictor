\# 🌾 Krishi Yield Predictor



A machine learning web application that predicts crop yield for Indian farmers

based on region, season, soil inputs, and weather conditions.



\## 🔗 Live Demo

https://cropyield-predictor-aygymgatanbnasbyftuwa3.streamlit.app/



\## 📌 Problem Statement

Indian farmers often lack data-driven tools to estimate expected crop yield

before harvest. This app provides yield predictions to help farmers make

informed decisions about crop selection and resource allocation.



\## 🏗️ Architecture

This project follows a clean client-server architecture:

Streamlit (Frontend) → HTTP POST → FastAPI (Backend) → ML Model



\- \*\*Frontend\*\* (app.py) — handles UI, collects inputs, displays results

\- \*\*Backend\*\* (main.py) — exposes REST API endpoint for predictions

\- \*\*Predictor\*\* (predictor.py) — loads models, handles encoding and prediction

\- \*\*Schemas\*\* (schemas.py) — validates incoming and outgoing data using Pydantic



\## 📁 Project Structure

crop\_yield\_predictor/

├── app.py           # Streamlit frontend

├── main.py          # FastAPI backend

├── predictor.py     # Model loading and prediction logic

├── schemas.py       # Pydantic input/output schemas

├── requirements.txt

└── README.md



\## 🚀 How to Run Locally



\*\*Step 1 — Clone the repository\*\*

```bash

git clone https://github.com/nishant-ethape/crop\_yield-predictor

cd crop\_yield\_predictor

```



\*\*Step 2 — Create and activate virtual environment\*\*

```bash

python -m venv venv

venv\\Scripts\\activate

```



\*\*Step 3 — Install dependencies\*\*

```bash

pip install -r requirements.txt

```



\*\*Step 4 — Start FastAPI backend\*\*

```bash

uvicorn main:app --reload

```



\*\*Step 5 — Start Streamlit frontend (new terminal)\*\*

```bash

streamlit run app.py

```



\*\*Step 6 — Open in browser\*\*

Streamlit → http://localhost:8501

FastAPI docs → http://localhost:8000/docs



\## 📊 Dataset

\- Source: Ministry of Agriculture and Farmers Welfare, Government of India

\- Records: 15,000+ entries across 37 crops and 30 Indian states

\- Time period: 1997–2021



\## 🧠 Models Trained

| Model | R² Score | RMSE |

|-------|----------|------|

| Linear Regression | 72.5% | 5.96 |

| Random Forest | 97.2% | 1.90 |

| XGBoost | 97.3% | 1.87 |



\*\*Final Model: XGBoost (97.3% R²)\*\*



\## ⚙️ Features Used

\- Crop type, State, Season, Year

\- Land area, Annual rainfall

\- Fertilizer and pesticide usage



\## 🛠️ Tech Stack

\- Python, Pandas, NumPy

\- Scikit-learn, XGBoost

\- FastAPI, Pydantic, Uvicorn

\- Streamlit



\## ⚠️ Known Limitations

\- State-level rainfall data used instead of district-level seasonal rainfall

\- Target encoding on Crop and State may introduce mild data leakage

\- Market price advisory module planned for Version 2



\## 🚀 Version 2 Roadmap

\- District-level seasonal rainfall integration

\- Mandi price advisory for optimal selling window

\- Leave One Out encoding to fix target leakage

\- Docker containerization for easier deployment

