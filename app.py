from flask import Flask, render_template, request
from flask_mysqldb import MySQL
app = Flask(__name__)

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'kp199814'
app.config['MYSQL_DB'] = 'remindify'

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        firstName = details['fname']
        lastName = details['lname']
        email = details['email']
        phone = details['phone']
        username = details['username']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users(firstName, lastName, username, email, phoneNumber) VALUES (%s, %s, %s, %s, %s)", (firstName, lastName, username, email, phone))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('index.html')
 
 
if __name__ == '__main__':
    app.run()