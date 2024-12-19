# Set the secret key to some random bytes. Keep this really secret!
from flask import Flask, redirect, request, render_template, make_response

app = Flask(__name__)


@app.route("/")
def index():
    username = get_session()
    if username:
        return f"Logged in as {username}"
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        resp = make_response(redirect("/"))
        resp.set_cookie("username", username)  # Set the cookie
        return resp
    return render_template("index.html")


@app.route("/logout")
def logout():
    resp = make_response(redirect("/"))
    resp.delete_cookie("username")  # delete the cookie
    return resp


def get_session():
    if request.cookies.get("username"):
        return request.cookies.get("username")
    return None


if __name__ == "__main__":
    app.run(port=5000)
