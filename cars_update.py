import sqlite3

with sqlite3.connect ("cars.db") as connection:

	c=connection.cursor()  # c cursor
	cars = [
			('Ford', 'Focus', 10),
			('Ford', 'F-150', 14),
			('Ford', 'Mustang', 5),
			('Honda', 'Civic', 4),
			('Honda', 'Fit', 20)
			]
	
	
	c.executemany("INSERT INTO inventory VALUES(?,?,?)", cars)
	
	c.execute("""SELECT model FROM inventory WHERE quantity >14""")
	print "/nNEW DATA /n"
	#c.execute (""" SELECT * FROM inventory""")
	rows=c.fetchall()
	
	for r in rows:
		print r [0]
		
		
	
	