# Install Mysql
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python


import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd='pandu21$'
)

# prepare a cursor object
cursorObject = dataBase.cursor()

# create a database
cursorObject.execute("CREATE DATABASE crmco")

print("All Databases Created")