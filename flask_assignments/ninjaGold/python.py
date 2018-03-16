from flask import Flask, render_template, request, session, redirect
import random
from datetime import datetime

app = Flask(__name__)
app.secret_key="ThisIsSecret"

@app.route('/')
def ninjagold():
    session.clear()
    session['gold'] = 0
    return render_template("index.html")

@app.route('/process_money', methods=['POST'])
def processmoney():
    try:
        temp = session['activity']
    except KeyError:
        temp = []

    if request.form['building'] == 'farm':
        result = random.randrange(10, 21)

    elif request.form['building'] == 'casino':
        result = random.randrange(-50, 50)

    elif request.form['building'] == 'cave':
        result = random.randrange(5, 11)
    else:
        result = random.randrange(2, 6)
    if result > 0:
        message = "you earned {} at {}".format(result, datetime.now().strftime("%H:%m:%p"))
    elif result == 0:
        message = "you broke even at the casino at {}".format(datetime.now().strftime("%H:%m:%p"))
    else:
        message = "you lost {} at {}".format(result, datetime.now().strftime("%H:%m:%p"))
    session['gold'] = int(session['gold']) + result
    temp.append(message)
    session['activity'] = temp
    return render_template('/index.html')



app.run(debug=True)