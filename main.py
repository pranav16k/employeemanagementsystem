from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# MySQL Configuration
db = mysql.connector.connect(
    host='127.0.0.1',
    user="root",
    password="adarsh",
    database="employeedb"
)

@app.route('/')
def index():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()
    return render_template('index.html', employees=employees)

if __name__ == '__main__':
    app.run(debug=True)
