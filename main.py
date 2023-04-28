
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
#___________________________MAIN_MENU___________________________

mainmenu = input("Welcome to Hazel's Bank!\nPlease state your Account Number:");
my_database.execute(f"SELECT * from bank.users WHERE Account_num='{mainmenu}';")

if my_database.fetchall():
    print("thank you!")

else:
    print("Sorry we don't have a customer by that ID number...")

#____________________________________Viewing Account________________________________

def find_user():

    viewacc = input("Please state your PIN number:");
    sql_statement = 'SELECT * FROM bank.users WHERE Pin='+viewacc+';'
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
    
    else:
        print("So sorry to hear that...\n")
        return find_user(), user_balance(), transact_hist()
user_balance()

#___________________________Viewing Transaction History________________________

def transact_hist():
    ask = input("Would you like to see your most recent transaction?(yes/no):")
    if ask == "yes":
        print("\n")
        transactions = 'SELECT * FROM bank.transactionhistory WHERE Account_num='+mainmenu+' ORDER BY DateTime DESC LIMIT 1;'
        my_database.execute(transactions)
        output = my_database.fetchone()
        for x in output:
            print(x)

    else:
        print("Alrighty")
transact_hist()

#________________________Transactiom function_______________________
def transact():
    import datetime
    
    ask3 = input("Would you like to make a transaction?(yes/no):")
    if ask3 == "yes":
        type = input("Will you be depositing or withdrawing today?(D/W):")
        amount = input("And how much would you like to deposit/withdraw: ")
        today = str(datetime.datetime.now())
        addData = 'INSERT INTO bank.transactionhistory(Account_num, Type, Amount, Datetime) VALUES ('+mainmenu+',"'+type+'",'+amount+',"'+today+'");'
        my_database.execute(addData)
        output = my_database.fetchall()
        print(output)

        connection.commit()
        print("Today's transaction has been added to your history!")
    else:
        print("Alrighty!\n")

transact()

#_________________________Adding New Memmber__________________________
from random import choice
import string

def newMember():
    ask2 = input("Thank you for your time\nWould you like to Logout or Add user(L/A):")
    if ask2 == "L":
        print("Bye")
        mainmenu = input("Welcome to Hazel's Bank!\nPlease state your Account Number:");
        my_database.execute(f"SELECT * from bank.users WHERE Account_num='{mainmenu}';")
        if my_database.fetchall():
            print("thank you!")
            return find_user(), user_balance(), transact(), transact_hist(), newMember()
        else:
             print("Sorry we don't have a customer by that ID number...")
    if ask2 == "A":
        addMember = input("Please state the NEW member's name:")
        strgnum = string.digits
        num =''.join(choice(strgnum) for _ in range(4))
        dob = input("State user's D.O.B:")
        pin = input("Pick a three digit Pin number:")
        addData = 'INSERT INTO bank.users (Account_num, Full_name, Pin, DOB) VALUES ('+num+', "'+addMember+'",'+pin+',"'+dob+'");'
        my_database.execute(addData)
        connection.commit()
        print("A new member has been added!\n"+addMember+"'s account number is:"+num+"\nThank you and have a nice day!")
newMember()