import sqlite3

with sqlite3.connect ("new.db") as connection:
	c=connection.cursor()
	c.execute("""SELECT population.city,population.population, regions.region FROM population, regions
				WHERE population.city=regions.city ORDER by population.city ASC""")
	rows=c.fetchall()
	
	for r in rows:
		print "CITY:"+r[0]
		print "POPULATION:" + str( r[1])
		print "REGION:" + r[2]
		print
		
		