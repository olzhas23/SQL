import sqlite3



with sqlite3.connect ("new.db") as connection:  #connecting to DB
	c=connection.cursor()  # c as a cursor
	#c.execute ("""CREATE TABLE regions (city TEXT, region TEXT)""")  # if we created DB already, we can just comment it out
	cities = [ 
				('New York City', 'Northeast'), 
				('San Francisco', 'West'), 
				('Chicago', 'Midwest'), 
				('Houston', 'South'), 
				('Phoenix', 'West'), 
				('Boston', 'Northeast'), 
				('Los Angeles', 'West'), 
				('Houston', 'South'), 
				('Philadelphia', 'Northeast'), 
				('San Antonio', 'South'), 
				('San Diego', 'West'), 
				('Dallas', 'South'), 
				('San Jose', 'West'), 
				('Jacksonville', 'South'), 
				('Indianapolis', 'Midwest'),
				('Austin', 'South'), 
				('Detroit', 'Midwest') 
				]

	c.executemany("INSERT INTO regions VALUES(?,?)", cities)  # inserting data into table
	c.execute("SELECT*FROM regions ORDER BY region ASC")  # here we sort the table ASC in ascending order
	rows=c.fetchall()  # we fetchall the data from table to variable rows.
	
	for r in rows:
		print r[0], r[1]
		
