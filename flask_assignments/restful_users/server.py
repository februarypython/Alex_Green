from flask import Flask, redirect, render_template, request, session
from mysqlconnection import MySQLConnector

app = Flask(__name__)
mysql = MySQLConnector(app, 'friendsdb')
app.secret_key="secrets"

@app.route('/users/')
def users():
    all_users = mysql.query_db("SELECT id, first_name, last_name, occupation, created_at, updated_at, date_format(created_at, '%M %D %Y') AS created_at FROM friends;")
    return render_template("index.html", all_users=all_users)

@app.route('/users/new')
def newuser():
    return render_template("new_user.html")

@app.route('/users/create', methods=['POST'])
def createuser():
    query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at)\
                    VALUES(:first, :last, :occupation, NOW(), NOW())"
    data = {
        "first": request.form['first_name'],
        "last": request.form['last_name'],
        "occupation": request.form['occupation']
    }
    mysql.query_db(query, data)
    return redirect('/users')

@app.route('/users/<id>')
def showuser(id):
    show_user = ("SELECT id, CONCAT(first_name, ' ', last_name) AS fullname, occupation, date_format(created_at, '%M %D %Y') AS createdate, date_format(updated_at, '%M %D %Y') AS updated_at\
                    FROM friends WHERE id = :some_id")
    value = {
            "some_id": id
    }
    friends = mysql.query_db(show_user, value)
    return render_template("show_user.html", friends=friends)

@app.route('/users/<id>/edit')
def edituser(id):
    query = ("SELECT id FROM friends WHERE id = :some_id")

    value = {
        "some_id": id
    }
    friends = mysql.query_db(query, value)
    friends = friends[0]
    return render_template("edit_user.html", friends=friends)

@app.route('/users/<id>/destroy')
def destroy(id):
    query = ("DELETE FROM friends WHERE id = :some_id")
    data = {
        "some_id": id
    }
    mysql.query_db(query, data)
    return redirect('/users')

@app.route('/users/<id>/update', methods=['POST'])
def updateuser(id):
    query = "UPDATE friends SET first_name = :first, last_name = :last, occupation = :occupation, updated_at = NOW() WHERE id = :id"
    data = {
        "first": request.form['first_name'],
        "last": request.form['last_name'],
        "occupation": request.form['occupation'],
        "id": id
    }
    mysql.query_db(query, data)
    return redirect('/users/'+ str(id))
    
app.run(debug = True)