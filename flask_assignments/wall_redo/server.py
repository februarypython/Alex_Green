from flask import Flask, redirect, session, flash, render_template, request
import re
import md5
from mysqlconnection import MySQLConnector

app = Flask(__name__)
app.secret_key="secrets"
mysql = MySQLConnector(app, 'thewall')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    if "users" in session:
        return redirect('/wall')
    else:
        return render_template("index.html")

@app.route('/newuser', methods=['POST'])
def newuser():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = md5.new(request.form['password']).hexdigest()
    query = "SELECT * FROM users WHERE email = :some_email"
    data = {"some_email": email}
    if len(mysql.query_db(query, data)) == 0:
        print "no user"
        if not EMAIL_REGEX.match(email):
            flash("not a valid email")
        if len(first_name) <1 or len(last_name) <1 or len(email) <1 or len(request.form['password']) <1:
            flash("all boxes must be filled out")
        if request.form['password'] != request.form['passconfirm']:
            flash("password and confirm must match")
            return redirect('/')
        else:
            new_user = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at)\
                        VALUES (:fname, :lname, :email, :pass, NOW(), NOW())"
            user_values = {
                "fname": first_name,
                "lname": last_name,
                "email": email,
                "pass": password
            }
            mysql.query_db(new_user, user_values)
            user = "SELECT * FROM users WHERE email = :email"
            values = {"email": email}
            users = mysql.query_db(user, values)
            session['users'] = users[0]
            return redirect('/wall')
    else:
        print "user exists"
        flash('user exists already')
    return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    password = md5.new(request.form['password']).hexdigest()
    query = "SELECT * FROM users WHERE email = :email LIMIT 1"
    values = {"email": request.form['email']}
    logincheck = mysql.query_db(query, values)
    if len(logincheck) == 0:
        print "email does not exist"
        return redirect('/')
    else:
        session['users'] = logincheck
        logincheck=logincheck[0]
        print "email DOES exist bruh"
        if logincheck['email'] == request.form['email'] and logincheck['password'] == password:
            return redirect('/wall')
        else:
            flash("login failed, bitch")
            return redirect('/')

@app.route('/wall')
def wall():
    usermessages = mysql.query_db("SELECT CONCAT(first_name, ' ', last_name) AS username, users.id as test, message, date_format(messages.created_at, '%M %D %Y') AS messagedate, messages.id AS idmessage FROM users\
                    JOIN messages ON users.id = messages.user_id;")
    usercomments = mysql.query_db("SELECT comment, comments.id, first_name, last_name, messages.id, comments.message_id\
                                FROM messages JOIN comments ON messages.id = comments.message_id JOIN users ON users.id = comments.user_id;")
    return render_template("wall.html", usermessages = usermessages, usercomments=usercomments)

@app.route('/messages', methods=['POST'])
def messages():
    messages = request.form['messages']
    query = "INSERT INTO messages (user_id, message, created_at, updated_at)\
            VALUES (:user_id, :message, NOW(), NOW())"
    data = {
        "user_id": session['users'][0]['id'],
        "message": messages
    }
    mysql.query_db(query, data)
    return redirect('/wall')

@app.route('/comments/<id>', methods=['POST'])
def comments(id):
    comments = request.form['comments']
    query = "INSERT INTO comments (user_id, message_id, comment, created_at, updated_at)\
            VALUES (:user_id, :message_id, :comment, NOW(), NOW())"
    data = {
        "user_id": session['users'][0]['id'],
        "message_id": id,
        "comment": comments
    }
    mysql.query_db(query, data)
    return redirect('/wall')

@app.route('/delete/<id>', methods=['POST'])
def delete(id):
    query = "DELETE FROM comments WHERE message_id = :id"
    data = {
        "id": id
    }
    query2 = "DELETE FROM messages WHERE id = :id"
    mysql.query_db(query, data)
    mysql.query_db(query2, data)
    return redirect('/wall')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
    
app.run(debug=True)