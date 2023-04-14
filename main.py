import mysql.connector

connection = mysql.connector.connect(user = "root", database = "example", password = "NaneLimonKabugu16^")

cursor = connection.cursor()

addData = ("INSERT INTO example (Idstudent, Age, Name) VALUES (4,"Jordan",12)")

cursor.execute(addData)

connection.commit()

cursor.close()

connection.close()