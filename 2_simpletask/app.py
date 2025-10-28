from flask import Flask

app = Flask(__name__)   # create a Flask app

@app.route("/")         # define a route (homepage)
def home():
    return "Hello, Flask!"   # response

if __name__ == "__main__":
    app.run(debug=True)   # run the app in debug mode
