# hello_flask.py - the smallest Flask web app
# Install once:  pip install flask
# Run:           python hello_flask.py   then open http://127.0.0.1:5000

from flask import Flask

app = Flask(__name__)          # create the web application

@app.route("/")                # when someone visits the home page "/"
def home():
    return "<h1>Hello from Flask!</h1><p>My first Python website.</p>"

@app.route("/about")           # a second page at /about
def about():
    return "This site is built in the Python module."

if __name__ == "__main__":
    app.run(debug=True)        # debug=True reloads when you save the file
