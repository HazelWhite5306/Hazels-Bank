
#addData = ("INSERT INTO school (Idstudent, Name, Age) VALUES (4, 'Jordan', 12)")

#cursor.execute(addData)

#connection.commit()

#testQuery = ("SELECT * FROM example.school")

#cursor.execute(testQuery)

#for item in cursor:

    #print(item)

import mysql.connector
connection = mysql.connector.connect(
         user = "root", 
         database = "bank", 
         password = "NaneLimonKabugu16^")
my_database = connection.cursor()
#___________________________MAIN_MENU_____________________________

mainmenu = input("Welcome to Hazel's Bank!\nPlease state your Account Number:");
if mainmenu == "1350" or "1401":
    print("Thank you!")
else:
    print("Sorry we don't have a customer by that ID number...")

#____________________________________Viewing Account________________________________

def find_user():

    viewacc = input("Please state your PIN number:");
    sql_statement = "SELECT * FROM bank.users WHERE Pin="+ viewacc +";"
    my_database.execute(sql_statement)
    output = my_database.fetchone()
    for x in output:
        print(x)

find_user()

#______________________________Viewing Account Balance_____________________

def user_balance():
    confirm = input("Is this you?(yes/no):");
    if confirm == "yes":
         print("Great!\n")
    
    name = input("State your Account name and we'll pull up your account information:");
    balancestatement = 'SELECT * FROM bank.accounts WHERE Acc_name="'+ name +'";'
    my_database.execute(balancestatement)
    output = my_database.fetchone()
    for x in output:
        print(x)
user_balance()

#___________________________Viewing Transaction History________________________

def transact_hist():
    ask = input("Would you like to see your most recent transaction?(yes/no):")
    if ask == "yes":
        print("\n")
        transactions = "SELECT * FROM bank.transactions WHERE Account_num="+ mainmenu +";"
        my_database.execute(transactions)
        output = my_database.fetchone()
        for x in output:
            print(x)
transact_hist()