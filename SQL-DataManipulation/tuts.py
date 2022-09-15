import mysql.connector
from datetime import datetime

mydb = mysql.connector.connect(host="localhost",user="abhisheknath",password="Abssyz@#42",
	   database="tutorial")

mycursor = mydb.cursor()

#$$$$ For Creating a Table $$$$#

#mycursor.execute("CREATE TABLE Person (name VARCHAR(50), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT )")
#mycursor.execute("CREATE TABLE Test (name varchar(50) NOT NULL, created datetime NOT NULL, gender ENUM('M', 'F', 'O') NOT NULL, id int PRIMARY KEY NOT NULL AUTO_INCREMENT)")

#$$$$ For viewing table attributes $$$$#

#mycursor.execute("DESCRIBE Person")

#$$$$  For inserting values $$$$#

# mycursor.execute("INSERT INTO Person (name,age) VALUES (%s, %s)", ("Khushi",23))
# mycursor.execute("INSERT INTO Test (name, created, gender) VALUES (%s,%s,%s)", ("Marie", datetime.now(), "O") )
# mydb.commit()


#$$$$  For Removing Values $$$$#

# mycursor.execute("ALTER TABLE Test DROP food")
# mycursor.execute("ALTER TABLE Test CHANGE name person_name VARCHAR(20)")


#$$$$  For Viewing Values $$$$#

# mycursor.execute("SELECT * from Person")
# mycursor.execute("SELECT * from Test WHERE gender = 'M' ORDER BY id DESC ")

#$$$$  For Modifying Data $$$$#

# mycursor.execute("ALTER TABLE Test ADD COLUMN food VARCHAR(50) NOT NULL")

#$$$$  For Iterating MyCursor $$$$#

# mycursor.execute("DESCRIBE Test")
# for x in mycursor:
# 	print(x)

# result = mycursor.fetchall()
# print(result)


