from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return "no ninjas here"

@app.route('/ninjas')
def alldudes():
    return render_template("index.html")

@app.route('/ninjas/<color>')
def ninjacolor(color):
    print color
    return render_template("colors.html", color=color)

app.run(debug=True)