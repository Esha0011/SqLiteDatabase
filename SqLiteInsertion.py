#!/usr/bin/python

#To insert data into Sqlite database - Movie Table
import sqlite3

conn = sqlite3.connect('Mydb.db')
print("Opened database successfully");

conn.execute("INSERT INTO MOVIEE (ID,NAME,ACTOR,ACTRESS,DIRECTOR,YEAR) \
      VALUES (11, 'Etharkum thuninthavan', 'Surya', 'Priyanka', 'Pandiraj', 2022 )");

conn.execute("INSERT INTO MOVIEE (ID,NAME,ACTOR,ACTRESS,DIRECTOR,YEAR) \
      VALUES (12, 'Paava Kathaigal', 'Gautham Menon', 'Anjali', 'Sudha Kongara', 2020 )");

conn.execute("INSERT INTO MOVIEE (ID,NAME,ACTOR,ACTRESS,DIRECTOR,YEAR) \
      VALUES (13, 'Mudhal Nee Mudivu Nee', 'Kishen Das', 'Darbuka Siva', 'Darbuka Siva', 2022 )");

conn.execute("INSERT INTO MOVIEE (ID,NAME,ACTOR,ACTRESS,DIRECTOR,YEAR) \
      VALUES (14, 'Oh Mana Penne', 'Harish Kalyan', 'Priya Bhavani Shankar', 'Kaarthikk Sundar', 2021 )");


conn.commit()
print("Records inserted successfully");
conn.close()