from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name", "Guest")  # Get data from form submission
        return render_template("greet.html", name=name)
    return render_template("index.html")

@app.route("/greet", methods=["GET"])
def greet():
    name = request.args.get("name", "Guest")  # Get data from query string
    return render_template("greet.html", name=name)

if __name__ == "__main__":
    app.run(debug=True)