from flask import Flask, render_template, redirect, request, flash, session
import re
app = Flask(__name__)
app.secret_key="SoSecret"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def processing():
    email = request.form['email']
    first = request.form['firstname']
    last = request.form['lastname']
    password = request.form['password']
    passconfirm = request.form['passconfirm']
    REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    PASSREGEX = re.compile('\d.*[A-Z]|[A-Z].*\d') #ninja
    if len(email) < 1 or len(last) < 1 or len(password) < 1 or len(passconfirm) < 1 or len(first) < 1:
        flash("All sections must be filled out")
        return render_template("index.html")

    elif not REGEX.match(email):
        flash("E-mail address is not valid")
        return redirect('/')
    
    elif not PASSREGEX.match(password): #ninja
        flash("Password must have at least 1 upper case letter and 1 number")
        return redirect('/')

    elif password != passconfirm:
        flash("Password confirm must match password")
        return redirect('/')

    elif len(password) <= 8 and len(passconfirm) <= 8:
        flash("Password must be at least 9 characters long")
        return redirect('/')

    elif first.isalpha() == False:
        flash ("Names must be letters only")
        return redirect('/')

    elif last.isalpha() == False:
        flash ("Names must be letters only")
        return redirect('/')
        
    else:
        return render_template('/results.html', first=first, last=last, email=email)

app.run(debug=True)