from flask import Flask, request, render_template_string

app = Flask(__name__)

# Home page with form
@app.route("/")
def home():
    html = """
    <h1>Welcome to the Greeting App!</h1>
    <form action="/greet" method="get">
        <label for="name">Enter your name:</label>
        <input type="text" id="name" name="name" placeholder="Your Name">
        <input type="submit" value="Greet Me">
    </form>
    """
    return render_template_string(html)

# Greet page
@app.route("/greet")
def greet():
    # Get query parameter 'name', default to 'Guest' if not provided
    name = request.args.get("name", "Guest")
    return f"<h1>Hello, {name}!</h1>"

if __name__ == "__main__":
    app.run(debug=True)
