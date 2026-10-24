# app.py - Flask with templates, URL variables, a form and a JSON API
# Run: python app.py   then open http://127.0.0.1:5000

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample data (in Session 08 this will come from a database)
courses = [
    {"id": 1, "name": "Python", "sessions": 16},
    {"id": 2, "name": "Flutter", "sessions": 18},
    {"id": 3, "name": "Dart", "sessions": 8},
]

# 1) Home page: send the list to an HTML template
@app.route("/")
def home():
    return render_template("index.html", courses=courses)

# 2) URL variable: /hello/Ali shows "Hello Ali"
@app.route("/hello/<name>")
def hello(name):
    return f"<h2>Hello {name}!</h2>"

# 3) Form: GET shows the form, POST receives the submitted data
@app.route("/contact", methods=["GET", "POST"])
def contact():
    message = ""
    if request.method == "POST":
        visitor = request.form["visitor_name"]
        message = f"Thank you {visitor}, we will contact you soon."
    return render_template("contact.html", message=message)

# 4) JSON API: useful for mobile apps (e.g. your Flutter app)
@app.route("/api/courses")
def api_courses():
    return jsonify(courses)

if __name__ == "__main__":
    app.run(debug=True)
