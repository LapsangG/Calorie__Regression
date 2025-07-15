# 🔥 Calorie Burn Prediction using Linear Regression

This project predicts the number of calories burned during physical activity using a Linear Regression model trained on exercise and biometric data. It includes data preprocessing, exploratory analysis, model training, evaluation, and deployment via a Streamlit web app.

---

## 📊 Project Overview

- **Problem Type**: Regression
- **Model Used**: Linear Regression
- **Dataset**: Combination of `calories.csv` and `exercise.csv`
- **Goal**: Predict the `Calories` burned based on features like:
  - Gender
  - Age
  - Height (cm)
  - Weight (kg)
  - Duration of Exercise (minutes)
  - Average Heart Rate (bpm)
  - Body Temperature (°C)

---

## 🧪 Project Workflow

1. **Data Loading & Merging**  
   Merged `exercise.csv` and `calories.csv` using `id`.

2. **Data Cleaning & Preprocessing**
   - Removed `User_ID`
   - Encoded `Gender`
   - Checked for nulls and data types

3. **Exploratory Data Analysis (EDA)**
   - Univariate, bivariate, and multivariate analysis (train/test split)
   - Heatmaps, pairplots, and distribution plots

4. **Model Training**
   - Linear Regression with `scikit-learn`
   - Feature-target split and train-test division

5. **Model Evaluation**
   - R² Score: ~0.967 (Train/Test)
   - MAE, MSE, RMSE metrics
   - Visualizations: Actual vs Predicted, Regression Lines

6. **Model Saving**
   - Trained model saved using `pickle` as `linear_regression_model.pkl`

7. **Deployment**
   - Streamlit app to predict calorie burn based on user input

---

## 🚀 Run the Streamlit App Locally

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/calorie-predictor.git
cd calorie-predictor
2. Create Virtual Environment (Recommended)
bash
Copy
Edit
python -m venv venv
source venv/bin/activate   # Or venv\Scripts\activate on Windows
3. Install Requirements
bash
Copy
Edit
pip install -r requirements.txt
4. Run the App
bash
Copy
Edit
streamlit run streamlit_app.py
📁 Project Structure
bash
Copy
Edit
calorie-predictor/
├── Caloriesburntpred.ipynb       # Jupyter notebook with full ML workflow
├── streamlit_app.py              # Streamlit web application
├── linear_regression_model.pkl   # Pickled trained model
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation


📚 Acknowledgements
Dataset from the Kaggle Exercise and Calories Dataset

Libraries used: pandas, numpy, scikit-learn, seaborn, matplotlib, streamlit

📬 Contact
Lapsang Lama
