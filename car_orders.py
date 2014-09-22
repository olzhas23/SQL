import sqlite3

with sqlite3.connect ("cars.db") as connection:
	c=connection.cursor()
	
	#c.execute ("""CREATE TABLE orders (make TEXT, order_date DATE)""")
	orders= [
				('Ford', '2014-02-02'),
				('Ford', '2014-02-05'),
				('Ford', '2014-02-12'),
				('Ford', '2014-02-02'),
				('Honda', '2014-02-05'),
				('Honda', '2014-02-02'),
				('Ford', '2014-04-02'),
				('Honda', '2014-02-04'),
			]
	c.executemany ("INSERT INTO orders VALUES(?, ?)", orders)
	
	data=c.fetchall()
	
	for r in data:
		print r[0]
		
		