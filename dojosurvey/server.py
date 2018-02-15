from flask import Flask, render_template, request, redirect, flash, session

app = Flask(__name__)
app.secret_key="asdf"

@app.route('/') 
def index():
    return render_template("index.html") 

@app.route('/process', methods=['POST'])
def process():
    location = request.form['location']
    favlang = request.form['favlang']
    comment = request.form['comment']
    name = request.form['name']
    if len(name) < 1 and len(comment) < 1:
        flash("Name and Comment cannot be empty")
        return render_template("/index.html")
    elif len(comment) < 1:
        flash("Comment cannot be empty")
        return render_template("/index.html")
    elif len(name) < 1:
        flash("Name cannot be empty")
        return render_template("/index.html")
    elif len(comment) > 120:
        flash("Comment is too long")
        return render_template("/index.html")
    else:
        return render_template('/result.html',  name=name, location=location, favlang=favlang, comment=comment)

app.run(debug=True)
