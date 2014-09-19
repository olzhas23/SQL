

# update and delete statements

import sqlite3

with sqlite3.connect("new.db") as connection:
	c=connection.cursor() # cursor to access data in the new.db
	# update data
	c.execute ("UPDATE population SET population =900000 WHERE city = 'New York'") 
	# delete data
	c.execute ("DELETE FROM population WHERE city ='Boston'")
	print ("\n NEW DATA:\n")  # header for the print out, to make it look good
	c.execute("SELECT * FROM population")  
	rows=c.fetchall()
	for r in rows:
		print r[0], r[1], r[2]
