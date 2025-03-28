from flask import Flask, render_template, request, redirect, url_for, session

from repositories import db_repo

app = Flask(__name__)
app.secret_key = "fdsafsdafadf"

@app.route('/')
def index():
    return render_template('index.html')

@app.post('/signup')
def signup():
    name = request.form['username']
    password = request.form['password']
    db_repo.signup_user(name, password)
    return redirect(url_for('login_page'))

@app.route('/home')
def home():
    name = session.get('name', None)
    if name == None:
        return redirect(url_for('index'))
    return render_template('main.html', username=name)

@app.route('/login_page')
def login_page():
    return render_template('login.html')

@app.post('/login')
def login():
    name = request.form['username']
    password = request.form['password']
    login, id, name = db_repo.login_user(name, password)
    if login == False:
        return redirect(url_for('login_page'))
    else:
        session['id'] = id
        session['name'] = name
        return redirect(url_for('home'))

@app.route('/logout')
def logout():
    for key in list(session.keys()):
        session.pop(key)
    return redirect(url_for('index'))