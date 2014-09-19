import sqlite3

with sqlite3.connect("new.db") as connection:
	c=connection.cursor()
	cities = [
				('Boston', 'MA', 699999),
				('Chicago', 'IL', 99999),
				('Houston', 'TX', 999999),
				('Arkansas','AZ', 44444)
				]
	c.executemany ('INSERT INTO population VALUES (?,?,?)', cities)
				
