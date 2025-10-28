# Form Submission

from flask import Flask, request, render_template

app = Flask(__name__)

# Home page
@app.route("/")
def home():
    return render_template("home.html")

# Login page
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        return f"<h1>Welcome, {username}!</h1><p>Your password is {password}</p>"
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)
