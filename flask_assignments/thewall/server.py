from flask import Flask, render_template, redirect, flash, session, request 
import re 
from mysqlconnection import MySQLConnector 
import md5 

app = Flask(__name__)
app.secret_key = "SuperTopSecret"
mysql = MySQLConnector(app, 'thewall') 
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register', methods=['POST'])
def register():
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    email = request.form['email']
    password = md5.new(request.form['password']).hexdigest()
    query = "SELECT * FROM users WHERE email = :some_email"
    data = {"some_email": email}
    if len(mysql.query_db(query, data)) == 0:
        if request.form['password'] != request.form['passconfirm']:
            flash("Password and confirm password must match")
            return redirect('/')
        elif not EMAIL_REGEX.match(email):
            flash("Email address is not valid")
            return redirect('/')
        elif len(firstname) < 2 or len(lastname) <2:
            flash("First and last names must be atleast 2 characters")
            return redirect('/')
        else:
            add_user = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at)\
                        VALUES (:firstname, :lastname, :email, :password, NOW(), NOW());"
            user_data = {
                "firstname": firstname,
                "lastname": lastname,
                "email": email,
                "password": password
            }
            mysql.query_db(add_user, user_data)
            user_query = "SELECT * FROM users where users.email = :email AND users.password = :password"
            query_data = {"email": email, 'password':password}
            user = mysql.query_db(user_query, query_data)
            
            session['user'] = user
            return redirect('/wall')
    else:
        flash("Email address is already registered")
        if flash:
            flash = flash
        return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    password = md5.new(request.form['password']).hexdigest()
    email = request.form['email']
    user_query = "SELECT * FROM users where users.email = :email"
    query_data = {"email": email}
    user = mysql.query_db(user_query, query_data)
    session['user'] = user
    if len(user) > 0:
        user = user[0]
        if password == user['password']:
                session['id'] = user['id']
                return redirect('/wall')   
        else:
            flash("bad password")
            return redirect('/')
    else:
        flash("username doesn't exist")
        return redirect('/')

@app.route('/wall')
def wall():
    usermessages = mysql.query_db("SELECT CONCAT(first_name, ' ', last_name) AS username, message, date_format(messages.created_at, '%M %D %Y') AS messagedate, messages.id FROM users\
                    JOIN messages ON users.id = messages.user_id;")
    usercomments = mysql.query_db("SELECT messages.user_id, comments.comment, comments.message_id, date_format(comments.created_at, '%M %D %Y') AS commentdate, messages.id, CONCAT(users.first_name, ' ',users.last_name) AS personname\
                                FROM messages LEFT JOIN comments ON messages.id = comments.message_id\
                                LEFT JOIN users ON comments.user_id = users.id;")
    return render_template("wall.html", usermessages=usermessages, usercomments=usercomments)

@app.route('/wallpost', methods=['POST'])
def wallpost():
    query = "INSERT INTO messages (user_id, message, created_at, updated_at)\
            VALUES (:some_user, :some_message, NOW(), NOW())"
    data = {
        "some_user": session['id'],
        "some_message": request.form['wall_post']
    }
    mysql.query_db(query, data)
    return redirect('/wall')

@app.route('/comment/<id>', methods=['POST'])
def comment(id):
    query = "INSERT INTO comments (user_id, message_id, comment, created_at, updated_at)\
            VALUES (:some_user, :some_message_id, :some_comment, NOW(), NOW())"
    data = {
        "some_user": session['id'],
        "some_message_id": id,
        "some_comment": request.form['comment']
    }
    mysql.query_db(query, data)
    return redirect('/wall')

app.run(debug=True)