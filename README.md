# 🏏 Cricket Player Performance Prediction (IPL)

## 📊 Project Overview
This project applies machine learning to historical IPL data (2008-2025) to predict individual player performance (runs for batsmen, wickets for bowlers) in upcoming matches. It aims to assist analysts and fantasy league players with data-driven insights.

## 🎯 Goals
1. **Predict Runs:** Estimate runs scored by a batsman in a specific match.
2. **Predict Wickets:** Estimate wickets taken by a bowler.
3. **Dashboard:** Deploy an interactive Streamlit app for users to query predictions.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Libraries:** Pandas, Scikit-learn, XGBoost, Streamlit, SHAP
* **Data Source:** Kaggle IPL Ball-by-Ball Dataset (2008-2025)

## 📂 Project Structure
* `data/`: Contains raw and processed datasets (ignored by git).
* `notebooks/`: Jupyter notebooks for EDA and Feature Engineering.
* `src/`: Python scripts for data cleaning and preprocessing.
* `models/`: Trained ML models (to be added).

## 🚀 Milestones
- [x] **Week 1:** Data Acquisition & Exploratory Data Analysis (EDA)
- [ ] **Week 2-4:** Feature Engineering & Preprocessing
- [ ] **Week 5-6:** Model Development (Random Forest, XGBoost)
- [ ] **Week 7-8:** Dashboard Deployment

## ⚙️ Setup & Installation
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
