import sqlite3  # importing sqlite3


with sqlite3.connect ("new_csv.db") as connection:  # connecting to new_csv.db
		c=connection.cursor()						# cursor to insert data
	
		names=[										# for big data files use lists
				('olzhas', 'shaikenov'),
				('dauren','asrymbetov')
				]
		c.executemany ('INSERT INTO employees VALUES (?,?)', names)  # executemany inserts big chunks of data format is INSERT INTO tablename VALUES (?, ?), listname
		
		rows=c.fetchall()  # fetchall retrieves all records from the DB, then we assign it to rows variable, then print all of them in the rows as a list
		
for r in rows:
		print r[0], r [1]
		

for row in c.execute ("SELECT firstname, lastname from employees"):  # printing the data from the DB while connected
		
		
		
		print (row)
		

