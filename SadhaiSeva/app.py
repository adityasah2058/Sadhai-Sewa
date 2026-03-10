from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="sadhai_sewa"
)
cursor = db.cursor()

# Home page
@app.route('/')
def home():
    return render_template('index.html')

# Join Us page
@app.route('/joinus')
def joinus():
    return render_template('joinus.html')

# Form submission
@app.route('/submit', methods=['POST'])
def submit():
    fullName = request.form['fullName']
    email = request.form['email']
    contact = request.form['contact']
    position = request.form['position']
    experience = request.form['experience']
    message = request.form['message']

    sql = """INSERT INTO joinus
             (fullName,email,contact,position,experience,message)
             VALUES (%s,%s,%s,%s,%s,%s)"""
    values = (fullName,email,contact,position,experience,message)
    cursor.execute(sql, values)
    db.commit()

    return redirect(url_for('joinus'))

if __name__ == '__main__':
    app.run(debug=True)