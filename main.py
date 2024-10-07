from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    greetings = "Witaj na mojej stronie"
    return greetings

@app.route('/me')
def pierwsza():
       return render_template("pierwsza.html")

@app.route('/contact', methods=['GET'])
def druga():
       return render_template("druga.html")