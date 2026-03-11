# Your final version without conflict markers
import os
from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open("energy_model.pkl","rb"))

@app.route("/")
def intro():
    return render_template("intro.html")

@app.route("/dashboard")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    hour = int(request.form["hour"])
    day = int(request.form["day"])
    month = int(request.form["month"])
    lag1 = 15000
    lag24 = 15000
    features = np.array([[hour, day, month, lag1, lag24]])
    prediction = model.predict(features)
    return render_template("index.html", prediction_text=f"Predicted Energy Consumption: {prediction[0]:.2f} MW")

port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port, debug=True)
