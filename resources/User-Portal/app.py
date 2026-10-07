from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)

app.secret_key = "my-secret-key"

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if username == "admin" and password == "1234":

            session["username"] = username

            return redirect("/dashboard")

        else:
            return "Invalid username or password"

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():

    if "username" not in session:
        return redirect("/login")

    return render_template("dashboard.html")


@app.route("/logout")
def logout():

    session.clear()

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
