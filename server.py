from flask import Flask, render_template, request
from database.db import *
app = Flask(__name__)

@app.route("/")
def home_func():
    return render_template("home.html")

@app.route("/register_page")
def register_page_func():
    return render_template("register.html")

@app.route("/register_user", methods=["post"])
def register_render_func():
    data = request.form
    id = data["id"]
    name = data["name"]
    lastname = data["lastname"]
    birthday = data["birthday"]
    add_user(id, name, lastname, birthday)
    return "the user was added"

@app.route("/consult_page")
def consult_page_func():
    return "Vista de consultar"

if __name__ == "__main__":
    host = "172.31.87.120"
    port = "80"
    app.run(host, port)