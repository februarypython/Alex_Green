from flask import Flask, redirect, render_template, flash, request, session
from mysqlconnection import MySQLConnector
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key="asdffasdfasf"

mysql = MySQLConnector(app, 'validation')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/submit', methods=['POST'])
def submit():
    email = request.form['email']
    query = "SELECT * FROM emails WHERE email_address = :some_email"
    data = {"some_email": email}
    email_check = mysql.query_db(query, data)
    session['name'] = request.form['email']

    if len(email_check) == 0:
        if not EMAIL_REGEX.match(email):
            flash("Invalid Email Address")
            return redirect('/')
        else:
            email_insert = "INSERT INTO emails (email_address, created_at, updated_at)\
                            VALUES (:some_email, NOW(), NOW())"
            mysql.query_db(email_insert, data)
        return redirect('/success')

    else:
        flash("Email address already exists")
        return redirect('/')

@app.route('/success')
def success():
    emails_added = mysql.query_db("SELECT id, email_address, date_format(created_at, '%c/%d/%y  %r') AS time_added FROM emails")
    return render_template("success.html", emails_added=emails_added, name=session['name'])

app.run(debug=True)