# # #Create a TABLE
# import sqlite3
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
#
# conn = sqlite3.connect('WhatsForDinner.db')
# print("Opened database successfully")
# conn.execute("INSERT INTO USER(USERNAME, PASSWORD, FIRST_NAME, LAST_NAME, ADRESS, TELEPHONE)\
#                VALUES ('BOB11', 'BOB123', 'BOB', 'DOE', 'PATRICKS STREET LIMERICK', '087158767')");
# conn.commit()
# print("Records created successfully")
# conn.close()
#
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
