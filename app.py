from flask import Flask, request, redirect
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy

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

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/login", methods=["POST"])
def validUser():
    
    return redirect('messageSchedule.html')


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

if __name__ == '__main__':
	app.run()
