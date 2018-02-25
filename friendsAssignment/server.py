from flask import Flask, render_template, redirect, request
from mysqlconnection import MySQLConnector
app = Flask(__name__)

mysql = MySQLConnector(app, 'friendsAssignment')

@app.route('/')
def index():
    friends = mysql.query_db("SELECT name, age, DATE_FORMAT(created_at, '%M %D') AS friend_since, \
                            DATE_FORMAT(created_at, '%Y') AS friend_year from friends;")
    return render_template("index.html", friends=friends)

@app.route('/add', methods=['POST'])
def add():
    query = "INSERT INTO friends (name, age, created_at, updated_at) \
            VALUES (:name, :age, NOW(), NOW())"
    data = {
        "name": request.form['friendname'],
        "age": request.form['friendage'],
    }
    mysql.query_db(query, data)
    return redirect ('/')

app.run(debug=True)