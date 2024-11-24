from flask import Flask, request, render_template, session, redirect, url_for
from datetime import timedelta


app = Flask("__name__")

app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(minutes=2)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["POST","GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form.get("name")
        session["user"] = user
        return redirect(url_for("user"))
    elif request.method == "GET":
        return render_template("index.html")
@app.route("/data")
def user():
    if "user" in session:
        user = session["user"]
        return render_template("second.html", placeholder=user)
    else:
        # Redirect to the login page if no user is in session
        return redirect(url_for("index"))
    
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug = True)