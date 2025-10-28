from flask import Flask, request, render_template

app = Flask(__name__)

# Home page with form
@app.route("/")
def home():
    return render_template("home.html")

# Greet page
@app.route("/greet")
def greet():
    name = request.args.get("name", "Guest")
    return render_template("greet.html", name=name)

if __name__ == "__main__":
    app.run(debug=True)
