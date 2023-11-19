from flask import Flask, request, redirect, session
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy
import scheduler.py

app = Flask(__name__)
app.debug = True

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

@app.route("/signup_redirect", methods=['GET', 'POST'])
def signup_redirect():

    if request.method == 'POST':
         return redirect(url_for('signup'))

    return render_template('signup_redirect.html')

@app.route("/login", methods=['GET',"POST"])
def validUser():
    username = request.form.get("username")
    password = request.form.get("password") 
    user = Profile.query.filter_by(username=username).first()
    if user and user.password == password:
            session['username'] = username
            # Passwords match, proceed with login
            return redirect('/message_schedule')
    else:
            # Incorrect username or password, handle accordingly
            return render_template('login.html')


@app.route("/login_redirect", methods=['GET', 'POST'])
def login_redirect():

    if request.method == 'POST':
         return redirect(url_for('login'))

    return render_template('login_redirect.html')

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
    
@app.route("/message_schedule", methods=["POST"])
def send_scheduled_texts():
    username = session.get('username')
    message = request.form.get("goal")
    time = request.form.get("time")
    user = Profile.query.filter_by(username = username).first()
    phone = user.phone
    try:
        scheduler.schedule_message(phone, time, message)
        return "done"
    except Exception as e:
        print(e)
        return "done"

if __name__ == '__main__':
	app.run()
