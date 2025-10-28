from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome!</h1><p>Go to /user/YourName</p>"

# Dynamic URL parameter
@app.route("/user/<name>")
def user_profile(name):
    return f"<h1>Hello, {name}!</h1><p>Welcome to your profile page.</p>"

if __name__ == "__main__":
    app.run(debug=True)
