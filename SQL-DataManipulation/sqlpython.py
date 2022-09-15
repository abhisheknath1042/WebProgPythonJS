import mysql.connector
from datetime import datetime

mydb = mysql.connector.connect(host="localhost",user="abhisheknath",password="Abssyz@#42",
	   database="newTut")

mycursor = mydb.cursor()

user_data = [("tim","techtim", "12345", "tim@gmail.com"),
		("rob", "rob123", "pass123", "rob@yahoo.com"),
		("julie", "jules69", "xx123xx", "julie@hotmail.com")]

user_scores =  [(45,100),
				(30,200),
				(46,124)]

# Q1 = "CREATE TABLE Users (id int PRIMARY KEY AUTO_INCREMENT NOT NULL, name VARCHAR(50) NOT NULL, userName VARCHAR(10) NOT NULL, password VARCHAR(12) NOT NULL, mailID VARCHAR(50) NOT NULL)"

# Q2 = "CREATE TABLE Scores (userID int PRIMARY KEY, FOREIGN KEY(userID) REFERENCES Users(id), game1 int DEFAULT 0, game2 int DEFAULT 0 )"

# mycursor.execute(Q1)
# mycursor.execute(Q2)


# mycursor.execute("SHOW TABLES")

# Q3 = "INSERT INTO Users (name, username, password, mailID) VALUES (%s,%s,%s,%s)"
# Q4 = "INSERT INTO Scores (userID, game1, game2) VALUES (%s,%s,%s)"

# for x,user in enumerate(user_data):
# 	mycursor.execute(Q3, user)
# 	last_id = mycursor.lastrowid
# 	mycursor.execute(Q4, (last_id,) + user_scores[x])

# mydb.commit()

#$$$$  For Iterating MyCursor $$$$#

# mycursor.execute("DESCRIBE Users")

mycursor.execute("SELECT * from Users")
for x in mycursor:
	print(x)

mycursor.execute("SELECT * from Scores")
for x in mycursor:
	print(x)

# result = mycursor.fetchall()
# print(result)
