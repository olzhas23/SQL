import sqlite3

conn=sqlite3.connect("new.db")

cursor=conn.cursor()


try:
	#insert data
	cursor.execute("""INSERT INTO population VALUE ('New York City', 'NY', 8999999)""")
	cursor.execute("""INSERT INTO population VALUE ('Denver', 'CO', 900000)""")
	
	# commit new changes
	
	conn.commit()
except sqlite3.OSError():
	print ("Opps Error, try again")
	
conn.close()

