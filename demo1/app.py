from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    name="Subi"
    students=["Raju","Sabu","Ramu"]
    return render_template('home.html',name=name,students=students)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/career')
def career():
    return render_template('career.html')

if __name__ == '__main__':
    app.run(debug=True)
    