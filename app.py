from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key ="JUNHAo98"

@app.route("/")
def index():
    flash("what's your name?")
    return render_template("index.html")

@app.route("/greet", methods=["POST", "GET"])
def greet():
    flash("Hi " + str(request.form['name_input']) + ", great to see you! I'm Jun Hao!")
    return render_template("index.html")