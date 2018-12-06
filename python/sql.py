#                                                                                   PYTHON + SQL3 LITE

# IMPORTING
import sqlite3
import csv

# CONNECTING SQL3
conn = sqlite3.connect('zoo.db')
c = conn.cursor()
#c.execute("""CREATE TABLE ZOOME
 #         ( animal TEXT,
 #           uniq_id INTEGER,
 #           water_needs INTEGER)""")
# OPPENING THE CSV FILE
with open ("zoo.csv") as zoofile:
    zooreader = csv.reader(zoofile,delimiter=",")
    next(zooreader)
    for row in zooreader:
            if len(row[2]) != 0:
                c.execute("""INSERT INTO ZOOME
                            VALUES('{}',{},{})"""
                          .format(row[0],row[1],row[2]))
            
        
  
c.execute("""SELECT * FROM ZOOME""")
print(c.fetchall())
