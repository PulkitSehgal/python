import sqlite3
import csv

conn2 = sqlite3.connect('list.db')
c2 = conn2.cursor()
c2.execute("""CREATE TABLE LISTME
             (StLastName TEXT,
               StFirstName TEXT,
               Grade INTEGER,
               Classroom INTEGER,
               Bus INTEGER)""")
    # OPPENING THE CSV FILE
with open ("list.csv") as zoofile:
    zooreader = csv.reader(zoofile,delimiter=",")
    next(zooreader)
    for row in zooreader:
            c2.execute("""INSERT INTO LISTME
                      VALUES('{}','{}',{},{},{})"""
                   .format(row[0],row[1],row[2],row[3],row[4]))
                
            
      
c2.execute("""SELECT * FROM LISTME""")
print(c2.fetchall())
