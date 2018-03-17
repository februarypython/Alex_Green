from flask import Flask, redirect, render_template, session, flash, request
import re
from mysqlconnection import MySQLConnector
import md5
import os, binascii

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key="SuperSecret"
mysql = MySQLConnector(app, 'login_registration')

@app.route('/')
def index():
    session.clear()
    return render_template("index.html")

@app.route('/create', methods=['POST'])
def create():
    email = request.form['email']
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    password = request.form['password']
    passconfirm = request.form['passconfirm']
    salt =  binascii.b2a_hex(os.urandom(15))
    hashed_pw = md5.new(password + salt).hexdigest()
    query = "SELECT * from users WHERE email = :some_email"
    data = {"some_email": email}
    email_check = mysql.query_db(query, data)
    if len(email_check) == 0:
        if not EMAIL_REGEX.match(email):
            flash("The email address provided is not valid")
        elif len(firstname) < 3 or len(lastname) < 3:
            flash("Names must be atleast 3 characters long")
        elif password != passconfirm:
            flash("Password and Confirm Password must match")
        elif len(password) < 8:
            flash("Password must be atleast 8 characters")
        else:
            add_user = "INSERT INTO users (firstname, lastname, email, password, created_at, updated_at, salt)\
                        VALUES (:firstname, :lastname, :email, :hashed_pw, NOW(), NOW(), :salt)"
            info = {
                "firstname": firstname,
                "lastname": lastname,
                "email": email,
                "hashed_pw": hashed_pw,
                "salt": salt
            }
            mysql.query_db(add_user, info)
            user_query = "SELECT * FROM users WHERE users.email = :email LIMIT 1"
            query_data = {"email": email}
            user = mysql.query_db(user_query, query_data)
            session['user'] = user
            return redirect('/welcome')
    else:
        flash("Email already exists")
        return redirect('/')

    return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    user_query = "SELECT * FROM users WHERE users.email = :email LIMIT 1"
    query_data = {"email": email}
    user = mysql.query_db(user_query, query_data)
    session['user'] = user
    if len(user) != 0:
        encrypted_password = md5.new(password +user[0]['salt']).hexdigest()
        if user[0]['password'] == encrypted_password:
            return redirect('/welcome')
        else:
            flash("incorrect password")
            return redirect('/')
    else:
        flash("invalid email")
        return redirect('/')

@app.route('/welcome')
def welcome():
    return render_template("welcome.html")

@app.route('/process')
def process():
    process_query = "SELECT * FROM "

app.run(debug=True)