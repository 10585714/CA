# Creating the database
import sqlite3
# conn = sqlite3.connect('WhatsForDinner.db')
#
# print("Opened database successfully")
#
# conn.execute('''CREATE TABLE PRODUCT
#       (ID INTEGER PRIMARY KEY AUTOINCREMENT,
#       NAME VARCHAR(50) NOT NULL,
#       DECS VARCHAR(50) NOT NULL,
#       CATERGORY VARCHAR(50) NOT NULL,
#       PRICE DECIMCAL(6) NOT NULL,
#       QUANTITY int NOT NULL);''')
# print("Table created successfully")
# conn.close()
#
# conn = sqlite3.connect('WhatsForDinner.db')
#
# print("Opened database successfully")
#
# conn.execute('''CREATE TABLE SHOPPING_SESSION
#       (SESSION_ID INTEGER PRIMARY KEY AUTOINCREMENT,
#       USERID INT NOT NULL,
#       TOTAL DECIMAL(6) NOT NULL DEFAULT '0.00',
#       CREATED_AT TIMESTAMP NOT NULL,
#       FOREIGN KEY (USERID) REFERENCES USER(USERID));''')
# print("Table created successfully")
# conn.close()
#
# conn = sqlite3.connect('WhatsForDinner.db')
#
# print("Opened database successfully")
#
# conn.execute('''CREATE TABLE Order_details
#       (ORDER_ID INTEGER PRIMARY KEY AUTOINCREMENT,
#       USERID INT NOT NULL,
#       TOTAL DECIMAL(6) NOT NULL DEFAULT '0.00',
#       PAYMENT_ID INT NOT NULL,
#       CREATED_AT TIMESTAMP NOT NULL,
#       FOREIGN KEY (USERID) REFERENCES USER(USERID));''')
# print("Table created successfully")
# conn.close()
#
# conn = sqlite3.connect('WhatsForDinner.db')
# print("Opened database successfully")
# cursor = conn.execute("SELECT * from Order_details")
# print("Operation done successfully")
# conn.close()
# #
# conn = sqlite3.connect('WhatsForDinner.db')
#
# print("Opened database successfully")
#
# conn.execute('''CREATE TABLE USER
#       (USERID INTEGER PRIMARY KEY AUTOINCREMENT,
#       USERNAME VARCHAR(30) NOT NULL,
#       PASSWORD VARCHAR (14) NOT NULL,
#       FIRST_NAME VARCHAR (15) NOT NULL,
#       LAST_NAME VARCHAR (20) NOT NULL,
#       ADRESS VARCHAR (30) NOT NULL,
#       TELEPHONE int NOT NULL,
#       USERTYPE VARCHAR(30));''')
#
# print("Table created successfully")
# conn.close()
#
# conn = sqlite3.connect('WhatsForDinner.db')
#
# print("Opened database successfully")
#
# conn.execute('''CREATE TABLE CART_ITEM
#       (CART_ITEMID INTEGER PRIMARY KEY AUTOINCREMENT,
#       SESSION_ID INT NOT NULL,
#       PRODUCT_ID INT NOT NULL,
#       QUANTITY INT NOT NULL,
#       FOREIGN KEY (PRODUCT_ID) REFERENCES PRODUCT(ID),
#       FOREIGN KEY (SESSION_ID) REFERENCES SHOPPING_SESSION(SESSION_ID));''')
# print("Table created successfully")
# conn.close()
#
#
# conn = sqlite3.connect('WhatsForDinner.db')
#
# print("Opened database successfully")
#
# conn.execute('''CREATE TABLE CONTACT
#       (CONTACTID INTEGER PRIMARY KEY AUTOINCREMENT,
#       NAME VARCHAR(30) NOT NULL,
#       EMAIL VARCHAR (23) NOT NULL,
#       MESSAGE VARCHAR (200) NOT NULL,
#       TELEPHONE int NOT NULL);''')
# print("Table created successfully")
# conn.close()
#
# conn = sqlite3.connect('WhatsForDinner.db')
#
# print("Opened database successfully")
#
# conn.execute('''CREATE TABLE PAYMENT_DETAILS
#       (PAYMENT_ID INTEGER PRIMARY KEY AUTOINCREMENT,
#       ORDER_ID INT NOT NULL,
#       AMOUNT INT NOT NULL,
#       STATUS VARCHAR(8) NOT NULL,
#       FOREIGN KEY (ORDER_ID) REFERENCES ORDER_DETAILS(ORDER_ID));''')
# print("Table created successfully")
# conn.close()
#
# conn = sqlite3.connect('WhatsForDinner.db')
#
# print("Opened database successfully")
#
# conn.execute('''CREATE TABLE ORDER_ITEMS
#       (ORDER_ITEMID INTEGER PRIMARY KEY AUTOINCREMENT,
#       USERID INT NOT NULL,
#       ORDER_ID INT NOT NULL,
#       CREATED_AT TIMESTAMP NOT NULL,
#       FOREIGN KEY (USERID) REFERENCES USER(USER_ID),
#       FOREIGN KEY (ORDER_ID) REFERENCES ORDER_DETAILS(ORDER_ID));''')
# print("Table created successfully")
# conn.close()

#Inserting all of the products avalible

# conn = sqlite3.connect('WhatsForDinner.db')
# print("Opened database successfully")
# #conn.execute("INSERT INTO PRODUCT(NAME, DECS, CATERGORY, PRICE, QUANTITY, CREATED_AT)\
# #              VALUES ('JANES PATISERY:COOKBOOOK', 'JANES PATISERY:COOKBOOOK', 'BOOK', 19.99, 20, '10:45')");
# conn.execute("INSERT INTO PRODUCT(ID, NAME, DECS, CATERGORY, PRICE, QUANTITY, CREATED_AT)\
#              VALUES (2, 'SWEET THERAPY: THE JOY OF BAKING', 'SWEET THERAPY: THE JOY OF BAKING', 'BOOK', 20.99, 35, '10:45')");
# conn.execute("INSERT INTO PRODUCT(ID, NAME, DECS, CATERGORY, PRICE, QUANTITY, CREATED_AT)\
#              VALUES (3, 'LILYS FAMILY FAVOURITES:COOKBOOOK', 'LILY FAMILY FAVOURITES:COOKBOOOK', 'BOOK', 18.99, 25, '10:45')");
# conn.execute("INSERT INTO PRODUCT(ID, NAME, DECS, CATERGORY, PRICE, QUANTITY, CREATED_AT)\
#              VALUES (4, 'THE VEG BOX:COOKBOOOK', 'THE VEG BOX:COOKBOOOK', 'BOOK', 19.99, 25, '10:45')");
# conn.execute("INSERT INTO PRODUCT(ID, NAME, DECS, CATERGORY, PRICE, QUANTITY, CREATED_AT)\
#              VALUES (5, 'CAN YOU MAKE THAT GLUTEN-FREE?-COOKBOOOK', 'CAN YOU MAKE THAT GLUTEN-FREE?:COOKBOOOK', 'BOOK', 18.99, 21, '10:45')");
# conn.execute("INSERT INTO PRODUCT(ID, NAME, DECS, CATERGORY, PRICE, QUANTITY, CREATED_AT)\
#              VALUES (6, 'THE FEMALE FACTOR:COOKBOOOK', 'THE FEMALE FACTOR:COOKBOOOK', 'BOOK', 21.99, 20, '10:45')");
# conn.execute("INSERT INTO PRODUCT(ID, NAME, DECS, CATERGORY, PRICE, QUANTITY, CREATED_AT)\
#              VALUES (7, '1 MONTH SUBSCRIPTION', '1 MONTH SUBSCRIPTION', 'SUBSCRIPTION', 5.99, 100, '10:45')");
# conn.execute("INSERT INTO PRODUCT(ID, NAME, DECS, CATERGORY, PRICE, QUANTITY, CREATED_AT)\
#              VALUES (8, '3 MONTH SUBSCRIPTION', '3 MONTH SUBSCRIPTION', 'SUBSCRIPTION', 17.99, 100, '10:45')");
# conn.execute("INSERT INTO PRODUCT(ID, NAME, DECS, CATERGORY, PRICE, QUANTITY, CREATED_AT)\
#              VALUES (9, '12 MONTH SUBSCRIPTION', '12 MONTH SUBSCRIPTION', 'SUBSCRIPTION', 50.00, 100, '10:45')");
# conn.commit()
# print("Records created successfully")
# conn.close()
#
# conn = sqlite3.connect('WhatsForDinner.db')
# print("Opened database successfully")
# cursor = conn.execute("SELECT * from PRODUCT")
# for row in cursor:
#     print("ID = ", row[0])
#     print("NAME = ", row[1])
#     print("DECS = ", row[2])
#     print("CATERGORY = ", row[3], "\n")
#     print("PRICE = ", row[4], "\n")
#     print("QUANTITY = ", row[5], "\n")
#     print("CREATED_AT = ", row[6], "\n")
#     print("Operation done successfully")
# conn.close()

#Test case Inserting the Users into the database

# conn = sqlite3.connect('WhatsForDinner.db')
# print("Opened database successfully")
# conn.execute("INSERT INTO USER(USERNAME, PASSWORD, FIRST_NAME, LAST_NAME, ADRESS, TELEPHONE, CREATED_AT)\
#                VALUES ('JANE123', 'HELLOJANE', 'JANE', 'DOE', 'HENRY STREET LIMERICK', '08715897', '10:45')");
# conn.execute("INSERT INTO USER(USERID, USERNAME, PASSWORD, FIRST_NAME, LAST_NAME, ADRESS, TELEPHONE, CREATED_AT)\
#               VALUES (2, 'JIM123', 'JIM60', 'JIM', 'DOE', 'CORK CITY, CORK LIMERICK', '08715897', '11:45')");
# conn.execute("INSERT INTO USER(USERID, USERNAME, PASSWORD, FIRST_NAME, LAST_NAME, ADRESS, TELEPHONE, CREATED_AT)\
#               VALUES (3, 'MARY123', 'LIMMARY', 'MARY', 'CONNOR', 'BALINGARRY, LIMERICK', '08715897', '10:45')");
# conn.commit()
# print("Records created successfully")
# conn.close()

#Test case 1.9
# conn = sqlite3.connect('WhatsForDinner.db')
# print("Opened database successfully")
# conn.execute("INSERT INTO USER(USERNAME, PASSWORD, FIRST_NAME, LAST_NAME, ADRESS, TELEPHONE)\
#                VALUES ('BOB11', 'BOB123', 'BOB', 'DOE', 'PATRICKS STREET LIMERICK', '087158767')");
# conn.commit()
# print("Records created successfully")
# conn.close()

# conn = sqlite3.connect('WhatsForDinner.db')
# print("Opened database successfully")
# cursor = conn.execute("SELECT * from USER")
# for row in cursor:
#     print("ID = ", row[0])
#     print("USER NAME = ", row[1])
#     print("PASSWORD = ", row[2])
#     print("FIRSTNAME = ", row[3], "\n")
#     print("LASTNAME= ", row[4], "\n")
#     print("ADRESS = ", row[5], "\n")
#     print("PHONE NUMBER = ", row[6], "\n")
#     print("Operation done successfully")
# conn.close()
#


#Test case 1.5 Contact form

# conn = sqlite3.connect('WhatsForDinner.db')
# print("Opened database successfully")
# conn.execute("INSERT INTO CONTACT(NAME, EMAIL, MESSAGE, TELEPHONE)\
#                VALUES ('Bob', 'BOB@gmail.com', 'TEST', '0962738374')");
# conn.commit()
# print("Records created successfully")
# conn.close()
#
# conn = sqlite3.connect('WhatsForDinner.db')
# print("Opened database successfully")
# cursor = conn.execute("SELECT * from CONTACT")
# for row in cursor:
#     print("ID = ", row[0])
#     print("NAME = ", row[1])
#     print("EMAIL = ", row[2])
#     print("MESSAGE = ", row[3], "\n")
#     print("TELEPHONE= ", row[4], "\n")
# conn.close()

# name='test1'
# email='test1@gmail.com'
# message='Test1'
# phone='testphone'
#
# def savecontact(name, email, message, phone):
#     con=sqlite3.connect("WhatsForDinner.db")
#     cur = con.cursor()
#     cur.execute("INSERT INTO CONTACT(NAME, EMAIL, MESSAGE, TELEPHONE) values (?,?,?,?)",(name, email, message, phone))
#     con.commit()
#     con.close()
#
# if savecontact(name, email, message, phone):
#     print('Message Added')
# else:
#     print('Message not deleted')
#
# conn = sqlite3.connect('WhatsForDinner.db')
# print("Opened database successfully")
# cursor = conn.execute("SELECT * from CONTACT")
# for row in cursor:
#     print("ID = ", row[0])
#     print("NAME = ", row[1])
#     print("EMAIL = ", row[2])
#     print("MESSAGE = ", row[3], "\n")
#     print("TELEPHONE= ", row[4], "\n")
# conn.close()

#Test Case 1.8
# conn = sqlite3.connect('WhatsForDinner.db')
# print("Opened database successfully")
# conn.execute("INSERT INTO USER(USERNAME, PASSWORD, FIRST_NAME, LAST_NAME, ADRESS, TELEPHONE, USERTYPE )\
#                VALUES ('Admin', 'Admin123', 'TEST', 'TEST', 'PATRICKS STREET LIMERICK', '087158767', 'A')");
# conn.commit()
# print("Records created successfully")
# conn.close()

#Test case 1.24
# conn = sqlite3.connect('WhatsForDinner.db')
# print("Opened database successfully")
# cursor = conn.execute("SELECT * from USER")
# for row in cursor:
#     print("ID = ", row[0])
#     print("USER NAME = ", row[1])
#     print("PASSWORD = ", row[2])
#     print("FIRSTNAME = ", row[3], "\n")
#     print("LASTNAME= ", row[4], "\n")
#     print("ADRESS = ", row[5], "\n")
#     print("PHONE NUMBER = ", row[6], "\n")
#     print("USER TYPE = ", row[7], "\n")
#     print("Operation done successfully")

#Test case 1.11

# def check_user(username, password):
#     con = sqlite3.connect('WhatsForDinner.db')
#     cur = con.cursor()
#     cur.execute('Select username,password FROM user WHERE username=? and password=?', (username, password))
#     result = cur.fetchone()
#     if result:
#         return True
#     else:
#         return False
#
# username='BOB'
# password='BOB123'
#
# if check_user(username, password):
#     print('User match')
# else:
#     print('User not matched')
#
# #Test case 1.12
#
# username = 'BOB-rand'
# password = 'BOB123'
#
# if check_user(username, password):
#     print('User match')
# else:
#     print('User not matched')
#
# #Test case 1.13
#
# username = 'BOB'
# password = 'BOB111'
#
# if check_user(username, password):
#     print('User match')
# else:
#     print('User not matched')
#
# #Test case 1.14
#
# username = 'BOB23'
# password = 'BOB111'
#
# if check_user(username, password):
#     print('User match')
# else:
#     print('User not matched')

#Test case 1.15

# con = sqlite3.connect('WhatsForDinner.db')
# print("Opened database successfully")
# cur = con.cursor()
# cursor = cur.execute("SELECT usertype from USER WHERE USERNAME='BOB'")
# result = cur.fetchone()
# admin = ('A',)
# print("USER TYPE = ", result[0])
# print(result)
# if result == admin:
#     print('Admin access')
# else:
#     print('Not Admin access')
# print("Operation done successfully")
# con.close()


# con = sqlite3.connect('WhatsForDinner.db')
# print("Opened database successfully")
# cur = con.cursor()
# cursor = cur.execute("SELECT usertype from USER WHERE USERNAME='BOB'")
# print(cursor)
# result = cur.fetchone()
# print(result)
# admin = ('A',)
# for result in cursor:
#     print("USER TYPE = ", result[0])
#     print(result)
#     admin = ('A',)
#     if result == admin:
#         print('Admin access')
#     else:
#         print('Not Admin access')
#     print("Operation done successfully")
# con.close()

# def check_user_type(username):
#     con = sqlite3.connect('WhatsForDinner.db')
#     print("Opened database successfully")
#     cur = con.cursor()
#     cursor = cur.execute("SELECT usertype from USER WHERE username=?",(username,))
#     print(username)
#     print(cursor)
#     result = cur.fetchone()
#     admin = ('A',)
#     print(result)
#     if result == admin:
#         print('Admin access')
#         return True
#     else:
#         print('Not Admin access')
#         return False
#
#     print("Operation done successfully")
#     con.close()
#

#Test case 1.16
# username='cleryruth@gmail.com'
# if check_user_type(username):
#     print('Admin acess')
# else:
#     print('No Acess')


#Test case 1.15
# # username='BOB'

# if check_user_type(username):
#     print('Admin acess')
# else:
#     print('No Acess')
#
# conn = sqlite3.connect('WhatsForDinner.db')
# print("Opened database successfully")
# cursor = conn.execute("SELECT * from USER WHERE USERTYPE='A'")
# for row in cursor:
#     print("ID = ", row[0])
#     print("USER NAME = ", row[1])
#     print("PASSWORD = ", row[2])
#     print("FIRSTNAME = ", row[3], "\n")
#     print("LASTNAME= ", row[4], "\n")
#     print("ADRESS = ", row[5], "\n")
#     print("PHONE NUMBER = ", row[6], "\n")
#     print("USER TYPE = ", row[7], "\n")
#     print("Operation done successfully")
#
# cursor = conn.execute("SELECT usertype from USER WHERE USERNAME='BOB'")
# for row in cursor:
#     print("Usertype = ", row[0])
#     print("Operation done successfully")
# conn.close()

# def deleterecord(id):
#     print(id)
#     with sqlite3.connect("WhatsForDinner.db") as con:
#         cur = con.cursor()
#         cursor = cur.execute("SELECT USERNAME from USER WHERE USERID=?",(id,))
#         result = cur.fetchone()
#         print(cursor)
#         print(result)
#         try:
#             cur = con.cursor()
#             print(id)
#             cur.execute("delete from user where USERID = ?", id)
#             msg = "record successfully deleted"
#             True
#         except:
#             msg = "This User can't be deleted"

#Test case 1.28

def deleterecord(id):
    with sqlite3.connect("WhatsForDinner.db") as con:
        try:
            cur = con.cursor()
            cur.execute("delete from USER where USERID = ?", id)
            msg = "record successfully deleted"
        except:
            msg = "can't be deleted"
id='1'

if deleterecord(id):
    print('User deleted')
else:
    print('User not deleted')

#Test case 1.29

id = '55'

if deleterecord(id):
    print('User deleted')
else:
    print('User not deleted')

