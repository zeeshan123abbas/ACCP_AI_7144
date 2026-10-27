# mini_project_flask_predictor.py - serve the saved iris model as a JSON API
# Run lab5_save_and_load_model.py first, then:  python mini_project_flask_predictor.py
# Try:  http://127.0.0.1:5000/predict?sl=5.1&sw=3.5&pl=1.4&pw=0.2

import joblib
from flask import Flask, jsonify, request

app = Flask(__name__)
model = joblib.load("iris_model.joblib")            # load ONCE when the app starts
SPECIES = ["setosa", "versicolor", "virginica"]


@app.route("/predict")
def predict():
    try:
        features = [[float(request.args["sl"]), float(request.args["sw"]),
                     float(request.args["pl"]), float(request.args["pw"])]]
    except (KeyError, ValueError):
        return jsonify({"error": "send numbers sl, sw, pl, pw"}), 400
    number = int(model.predict(features)[0])
    confidence = float(model.predict_proba(features)[0][number])
    return jsonify({"species": SPECIES[number], "confidence": round(confidence, 3)})


if __name__ == "__main__":
    app.run(debug=True)
