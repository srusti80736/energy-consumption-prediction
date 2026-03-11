Energy Consumption Prediction 
A Machine Learning project that predicts electricity consumption using historical hourly energy data.
**Project Overview:**
This project builds a regression model to predict future electricity consumption based on historical energy usage patterns. The system uses time-based features such as hour, day of week, and month along with lag features.
The trained model is deployed using a Flask web application where users can input time parameters and get predicted energy consumption.
1.Dataset
Dataset used: Hourly Energy Consumption Dataset
Source: https://www.kaggle.com/datasets/robikscube/hourly-energy-consumption
Example dataset used in this project:
AEP_hourly.csv
2.Machine Learning Pipeline
  1. Data Loading
  2. Data Cleaning
  3. Feature Engineering
  4. Model Training
  5. Model Evaluation
  6. Model Selection
  7. Model Deployment (Flask Web App)
3.Feature Engineering
The following features are used:
- Hour
- Day of Week
- Month
- Lag1 (previous hour energy)
- Lag24 (previous day energy)
4.Models Used
- Linear Regression
- Random Forest Regressor
Used conditional statements to compare the values of model evaluation(RMSE and MSE) to choose the best model
Model performance is evaluated using:
- RMSE (Root Mean Square Error)
- MAE (Mean Absolute Error)
5.Project Structure
  energy-consumption-prediction
│
├── dataset
│ └── AEP_hourly.csv
│
├── static
│ ├── style.css
│ ├── intro.css
│ └── intro.js
│
├── templates
│ ├── intro.html
│ └── index.html
│
├── app.py
├── model.py
├── extract.py
├── requirements.txt
└── README.md
|__energy-consumption-prediction
│
├── dataset
│ └── AEP_hourly.csv
│
├── static
│ ├── style.css
│ ├── intro.css
│ └── intro.js
│
├── templates
│ ├── intro.html
│ └── index.html
│
├── app.py
├── model.py
├── extract.py
├── requirements.txt
└── README.md
|__requirments.txt

Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Flask
- Matplotlib
Future Improvements
- Time series forecasting using ARIMA
- Deep learning models like LSTM
- Real-time energy consumption dashboard
Author
Srusti K
Live demo Link : http://127.0.0.1:5000
