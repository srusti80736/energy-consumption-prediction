import os
from flask import Flask, render_template, request
import pickle
import numpy as np

# Create Flask app
app = Flask(__name__)

# Load trained model
model = pickle.load(open("energy_model.pkl","rb"))

# Intro landing page
@app.route("/")
def intro():
    return render_template("intro.html")

# Dashboard page
@app.route("/dashboard")
def home():
    return render_template("index.html")

# Prediction route
@app.route("/predict", methods=["POST"])
def predict():

    # Get user input
    hour = int(request.form["hour"])
    day = int(request.form["day"])
    month = int(request.form["month"])

    # Since lag features are not provided by user
    # we simulate them with average values
    lag1 = 15000
    lag24 = 15000

    features = np.array([[hour, day, month, lag1, lag24]])

    # Predict energy consumption
    prediction = model.predict(features)

    return render_template(
        "index.html",
        prediction_text=f"Predicted Energy Consumption: {prediction[0]:.2f} MW"
    )

# Run server
if __name__ == "__main__":
    app.run(debug=True)
port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)
