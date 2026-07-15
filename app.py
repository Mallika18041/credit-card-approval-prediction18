from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load("model.pkl")

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = ""

    if request.method == "POST":
        age = int(request.form["age"])
        income = int(request.form["income"])
        credit_score = int(request.form["credit_score"])

        result = model.predict([[age, income, credit_score]])

        if result[0] == 1:
            prediction = "✅ Credit Card Approved"
        else:
            prediction = "❌ Credit Card Rejected"

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)