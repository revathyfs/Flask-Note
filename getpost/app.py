from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")  # Home page

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        return f"<h1>Welcome, {username}!</h1><p>Your password is {password}</p>"
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)
