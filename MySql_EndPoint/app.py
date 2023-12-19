from flask import Flask, request
import mysql

app = Flask(__name__)

# MySql Connection COnfiguration
db = mysql.connector.connect(
    host="localhost",
    user = "root",
    password="MySql@123",
    database="sample_db"
)
cursor = db.cursor()

# Endpoint to insert data into the table
@app.route('/execute_insert', methods=['POST'])
def insert():
    data = request.get_json()
    columns = ','.join(*data.keys())
    values = ','.join(*data.values())
    query = f"INSERT INTO users ({columns}) VALUES ({values})"
    cursor.execute(query)
    db.commit()
    return 'Data Inserted Successfully'

if __name__=='__main__':
    app.run(debug=True)

