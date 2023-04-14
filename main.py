import mysql.connector

connection = mysql.connector.connect(user = "root", database = "example", password = "NaneLimonKabugu16^")

cursor = connection.cursor()

#addData = ("INSERT INTO school (Idstudent, Name, Age) VALUES (4, 'Jordan', 12)")

#cursor.execute(addData)

#connection.commit()

testQuery = ("SELECT * FROM example.school")

 

cursor.execute(testQuery)

 

for item in cursor:

    print(item)

cursor.close()

connection.close()