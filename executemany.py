import sqlite3

with sqlite3.connect ("new.db") as connection:
	c=connection.cursor ()
	
	cities = [
				('Boston', 'MA', 555555),
				('Los Angeles', 'LA', 44444),
				('Houston', 'TX', 444444),
				('Philadelphia', 'PA', 1500000), 
				
				]
	c.executemany ("INSERT INTO population VALUES (?,?,?)", cities)
	c.execute ("SELECT*FROM population WHERE population > 900000")
	rows=c.fetchall()
	
	for r in rows:
		print r [0], r [1], r [2]
		
	
	