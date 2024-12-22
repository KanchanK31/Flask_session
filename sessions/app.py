from flask import Flask, redirect, request, render_template, make_response
import session

app = Flask(__name__)


@app.route("/")
def index():
    session_id = request.cookies.get("session_id")
    # get session data for session_id
    session_obj = session.get_session(session_id)
    if session_obj and session_obj.get("username"):
        return f"Logged in as {session_obj.get('username')}"
    # if no session found redirect to login screen.
    return render_template("login.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        age = request.form["age"]
        resp = make_response(redirect("/"))
        # set session with given data.(generate session_id, assign expiry time, store data)
        session.set_session({"username": username, "age": age}, resp)
        return resp
    return render_template("index.html")


@app.route("/logout")
def logout():
    resp = make_response(redirect("/"))
    # delete cookies for given session-id
    resp.delete_cookie("session_id")
    return resp


if __name__ == "__main__":
    app.run(port=5000)
