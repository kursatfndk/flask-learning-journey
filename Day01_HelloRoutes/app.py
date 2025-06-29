from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)



@app.route("/hello")
def hello():
    return render_template("hello.html")

@app.route("/hello-admin")
def hello_admin():
    return render_template("hello-admin.html")

@app.route("/hello-user/<name>")
def helloUser(name):
    if name.lower() == "admin":
        return redirect(url_for("hello_admin"))
    return render_template("hello_user.html", username=name)

@app.route("/login", methods=["POST",])
def login():
    if request.method == "POST":
        username = request.form["username"]
        return redirect(url_for("helloUser", name=username))
    else:
        return render_template("login.html")
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")
