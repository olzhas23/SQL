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
	c.execute ("SELECT * FROM inventory ORDER BY make ASC")
	rows=c.fetchall()
	
	for r in rows:
		print "MAKE MODEL QUANTITIY :" + r[0] +r [1] + str( r[2])
		#print "MODEL :" + r[1]
		#print "QUANTITIY :" + str(r[2])
		
	
	