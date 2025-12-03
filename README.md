🚀 Customer Churn Prediction Web Application

An end-to-end machine learning powered analytics system designed to predict customer churn, visualize model performance, and provide insights into customer retention patterns.

This project includes:

🎯 Binary churn prediction model (Retained = 0, Churned = 1)

📊 Interactive web UI for upload → preprocess → train → evaluate

🧠 Machine learning pipeline (feature engineering + encoding + model training)

📈 Confusion Matrix, ROC Curve, Feature Importance visuals

🗂️ Clean, modular backend for deployment & production use

🔍 Project Overview

Customer retention is one of the most critical challenges for subscription-based businesses.
This web application allows users to:

Upload their Telco Customer dataset

Automatically preprocess it

Train a churn prediction model

View performance metrics and visualizations

Understand top features that influence churn

The app is powered by Logistic Regression and optionally Random Forest, built on the popular Telco Customer Churn dataset (7043 rows × 51 columns).

🧠 Machine Learning Workflow
✔️ 1. Data Preprocessing

Handle missing values

Convert numeric-like strings to numeric

Label-encode & one-hot encode categorical features

Drop leakage columns (Customer Status, Churn Reason, Churn Score, etc.)

Normalize numeric features

Map Customer Status → binary target (0 = Retained, 1 = Churned)

✔️ 2. Model Training

Models used:

Logistic Regression (primary model)

RandomForestClassifier (for feature importance & comparison)

Training:

Train/Test Split: 80/20

Random State: 45

Max Iterations: 2000 (for logistic regression)

✔️ 3. Evaluation Metrics

The application displays:

Accuracy

Precision

Recall

F1 Score

ROC-AUC Score

Confusion Matrix

Classification Report

Top Feature Importances (Random Forest)

These metrics help evaluate how well the model predicts churn vs retention.

🖥️ Web Application Flow
1️⃣ Upload Dataset

Upload a .csv or .zip file containing the Telco dataset.
The app checks row & column count and validates structure.

2️⃣ Preprocessing

Shows steps like:

Handling missing values

Encoding categorical variables

Normalization

Feature engineering

Target creation

3️⃣ Model Training

Displays:

Algorithm used

Train/Test split

Iterations

Random state

4️⃣ Results Dashboard

Includes:

Confidence metrics

Confusion matrix heatmap

ROC curve

Feature importance graph

Prediction insights



📊 Sample Results

Accuracy: ~96%
Precision: ~96%
Recall: ~96%
F1 Score: ~96%
ROC-AUC: ~0.98

These numbers can vary depending on dataset composition and preprocessing.

🔧 Tech Stack

Python (Pandas, NumPy, Scikit-Learn, Matplotlib, Seaborn)

Machine Learning Models:

Logistic Regression

Random Forest

Frontend:

HTML / CSS / React / Emergent UI

Backend:

Flask / FastAPI (depending on your setup)

📦 Installation & Setup
Clone the repository:
git clone https://github.com/your-username/Customer-Churn-Prediction.git
cd Customer-Churn-Prediction

Install dependencies:
pip install -r requirements.txt

Run the backend:
python train_churn_binary.py

Launch the web application:
python main.py

🧪 Future Enhancements

Add XGBoost / LightGBM models

Add hyperparameter tuning

Add live predictions endpoint

Deploy to Render / Vercel / Heroku

Add automated EDA report generation

🙌 Acknowledgements

Dataset: IBM Telco Customer Churn Dataset
UI Framework: Emergent UI

⭐ Show Your Support

If you like this project, give it a ⭐ on GitHub!
It helps others discover it and motivates more work on ML/AI projects.
Note - Their is data leakage and I am trying to improve it and experimenting wiith Machine learnig algorithams so stay tuned
