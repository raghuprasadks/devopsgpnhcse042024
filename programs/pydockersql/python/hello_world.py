import mysql.connector

connection = mysql.connector.connect(
    user='root', password='root', host='mysql', port="3307", database='db')
print("DB connected")

cursor = connection.cursor()
cursor.execute('Select * FROM students')
students = cursor.fetchall()
connection.close()

print(students)