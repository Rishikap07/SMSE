import mysql.connector 

connection = mysql.connector.connect(
    host='localhost',
    database='sdp',
    user='root',
    password='admin'
)

if connection.is_conneted():
    print("sucessfully connected to the database")
    