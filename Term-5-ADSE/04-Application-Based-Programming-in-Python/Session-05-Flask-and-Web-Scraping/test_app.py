# test_app.py - test the Flask app WITHOUT opening a browser

from app import app

client = app.test_client()          # a fake browser provided by Flask

response = client.get("/")
print("Home status:", response.status_code)          # 200 means OK

response = client.get("/api/courses")
print("API data:", response.get_json())

response = client.post("/contact", data={"visitor_name": "Hira"})
print("Form reply contains thanks?", b"Thank you Hira" in response.data)
