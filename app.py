from flask import Flask, request, redirect, session
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy
import scheduler
import demotivation
from datetime import datetime, timedelta, timezone
import pytz



app = Flask(__name__)
app.debug = True
app.secret_key = 'HELLO'

# adding configuration for using a sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# Creating an SQLAlchemy instance
db = SQLAlchemy(app)

# Models
class Profile(db.Model):
    __tablename__ = 'profile'
    id = db.Column(db.Integer,nullable=False, primary_key=True)
    first_name = db.Column(db.String(20), unique=False, nullable=True)
    last_name = db.Column(db.String(20), unique=False, nullable=True)
    phone = db.Column(db.String(20), unique=True, nullable=True)
    username = db.Column(db.String(20), unique=True, nullable=True)
    password = db.Column(db.String(20), unique=True, nullable=True)

with app.app_context():
    # Create the tables
    db.create_all()

@app.route("/")
def home():
    return render_template('index2.html') 

@app.route("/signup")
def signup():
    return render_template('signup.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/message_scheduler")
def show(): 
    return render_template('message_scheduler.html')

@app.route("/login", methods=['GET',"POST"])
def validUser():
    username = request.form.get("username")
    password = request.form.get("password") 
    user = Profile.query.filter_by(username=username).first()
    if user and user.password == password:
            session['username'] = username
            return redirect('/message_scheduler')
    else:
            error_message = "Login failed, incorrect username or password, please try again."
            return render_template('login.html', error_message=error_message)

@app.route('/signup', methods=["POST"])
def profile():
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    username = request.form.get("username")
    phone = request.form.get("phone_number")   
    password = request.form.get("password")

    if first_name != '' and last_name != '' and phone != '' and password != '':
        p = Profile(first_name=first_name, last_name=last_name, phone=phone, username=username, password=password)
        db.session.add(p)
        db.session.commit()
        return redirect('/login')
    else:
        return redirect('/')
    
@app.route("/message_scheduler", methods=["GET", "POST"])
def send_scheduled_texts():
    username = session.get('username')
    message = request.form.get("goal")
    message = message + " Your motivation for the day: " + demotivation.return_demotivation()
    date = request.form.get("date")
    time = request.form.get("time")
    future = date + ' ' + time
    date_format = "%Y-%m-%d %H:%M"
    utc_timezone = pytz.timezone('UTC')
    date_object = datetime.strptime(future, date_format).astimezone(utc_timezone)
    user = Profile.query.filter_by(username = username).first()
    phone = user.phone
    try:
        scheduler.schedule_message(phone, message, date_object)
        return "done"
    except Exception as e:
        print(e)
        return "done"

if __name__ == '__main__':
	app.run()

