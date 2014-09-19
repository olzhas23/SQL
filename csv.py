

import csv
import sqlite3

with sqlite3.connect ("employees.db") as connection:
	c=connection.cursor()
	# open csv file and assign to variable for ease of the use
	employees=csv.reader(open("employees.csv", "rU"))
	c.execute("""CREATE TABLE employees(First Name TEXT, Last Name TEXT)""")
	c.executemany("INSERT INTO employees(First Name,Last Name) values (?,?)",employees)
	
	
	