from flask import Flask

app = Flask(__name__)

# Home route
@app.route("/")
def home():
    return "<h1>Welcome to My Website</h1><p>This is the homepage.</p>"

# About route
@app.route("/about")
def about():
    return "<h1>About Us</h1><p>This page gives information about the site.</p>"

# Contact route
@app.route("/contact")
def contact():
    return "<h1>Contact Us</h1><p>Email: hello@example.com</p>"

if __name__ == "__main__":
    app.run(debug=True)
