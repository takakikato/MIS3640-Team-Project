from flask import Flask, render_template, request
import requests
from A import get_recipie, nutrition

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template("welcome.html")

@app.route("/search/, methods=["GET", "POST"]")
    def search():
        if request.method == "POST":
            