import sqlite3



with sqlite3.connect ("cars.db") as connection:

	c=connection.cursor()
	
	c.execute("""SELECT DISTINCT inventory.quantity, inventory.Model, inventory.Make FROM inventory, orders WHERE 
					inventory.model = orders.make ORDER BY inventory.model """)
	rows=c.fetchall()
	
	
	
	sql = {'count' : "SELECT count (order_date) FROM orders WHERE make = 'Ford' ",
			'count' : "SELECT count (order_date) FROM orders WHERE make = 'Honda' "}
			
	
			
	for r in rows:
	
		print "Make : " + r[1] + " Model : " + r[2]
		print "Quantity :  "+ str (r[0])
	
	for keys, values in sql.iteritems():
		
		c.execute(values)
		
		result=c.fetchone()
		print
		print "ORDERS: " + str( result[0])
	