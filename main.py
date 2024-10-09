from flask import Flask
from flask import render_template
from flask import request
from flask import redirect

app = Flask(__name__)

@app.route('/')
def homepage():
    greetings = "Witaj na mojej stronie"
    return greetings


@app.route('/me')
def pierwsza():
       return render_template("pierwsza.html")

@app.route('/contact', methods=['GET', 'POST'])
def contact():
   if request.method == 'GET':
       print("We received GET")
       return render_template("druga.html")
   elif request.method == 'POST':
       print("We received POST")
       print(request.form)
       return redirect("/contact")