from flask import Flask, render_template

app = Flask(__name__)   # create a Flask app

@app.route("/")         # define a route (homepage)
def home():
    return render_template("index.html",name="Revathy")   # response

if __name__ == "__main__":
    app.run(debug=True)   # run the app in debug mode
