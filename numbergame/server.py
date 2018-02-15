from flask import Flask, render_template, redirect, session, request
app=Flask(__name__)
app.secret_key = "soSecret"

@app.route('/')
def index():
    import random
    session['number'] = random.randrange(0, 101)
    return render_template("index.html", number=session['number'])

@app.route('/guess', methods=['POST'])
def guessing():
    guess = request.form['guess']
    guess = int(guess)
    numb = session['number']
     # print guess, "my guess" ALL COMMENTS WERE USED FOR TESTING
    # print numb
    # if guess > session['number']:
    #     print "too high"
    # elif guess < session['number']:
    #     print "too low"
    # else: 
    #     print "bingo"

    return render_template("game.html", guess=guess, number=session['number'])
    


app.run(debug=True)