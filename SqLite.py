#!/usr/bin/python
# To create a table named MOVIE in SqLite database
#TABLE NAME = MOVIEE
#DATABASE NAME = Mydb
import sqlite3

conn = sqlite3.connect('Mydb.db')
print("Welcome to SqLite Database!")
print("Opened database successfully");

conn.execute('''CREATE TABLE MOVIEE
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         ACTOR           TEXT     NOT NULL,
         ACTRESS          TEXT     NOT NULL,
         DIRECTOR         TEXT     NOT NULL,
         YEAR           INT        NOT NULL);''')
print("Table created successfully");

conn.close()