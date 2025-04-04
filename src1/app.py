from flask import Flask, request, render_template
from pickle import load

app = Flask(__name__)
model = load(open("../models/DecisionTreeOptimized.sav", "rb"))


@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        val1 = float(request.form["Pregnancies"])
        val2 = float(request.form["Glucose"])
        val3 = float(request.form["BloodPressure"])
        val4 = float(request.form["SkinThickness"])
        val5 = float(request.form["Insulin"])
        val6 = float(request.form["BMI"])
        val7 = float(request.form["DiabetesPedigreeFunction"])
        val8 = float(request.form["Age"])

        data = [[val1, val2, val3, val4, val5,val6,val7,val8]]
        prediction = int(model.predict(data)[0])

    else:
        prediction = -1
    return render_template("index.html", prediction = prediction)