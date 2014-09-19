

import sqlite3 # Importing sqlite3 package to this program

conn=sqlite3.connect("cars.db") # creating/ connecting to DB cars.db

cursor=conn.cursor() # creating the cursor.  

cursor.execute("""CREATE TABLE inventory (Model TEXT, Make TEXT, Quantity INT)""") # then cursor makes the table	

conn.close()  #close DB
