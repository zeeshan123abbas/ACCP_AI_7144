# test_predictor.py - test the prediction API without a browser
from mini_project_flask_predictor import app

client = app.test_client()
print(client.get("/predict?sl=5.1&sw=3.5&pl=1.4&pw=0.2").get_json())
print(client.get("/predict?sl=6.7&sw=3.0&pl=5.2&pw=2.3").get_json())
print("Bad input status:", client.get("/predict?sl=abc").status_code)
