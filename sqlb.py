import sqlite3

conn=sqlite3.connect("new.db") # creating DB

cursor=conn.cursor()

cursor.execute("""INSERT INTO population VALUES('New York City', 'NY', 8200000)""")

cursor.execute("""INSERT INTO population VALUES('SanFran', 'SF', 820002300)""")
cursor.execute("""INSERT INTO population VALUES('Washington', 'DC', 820003400)""")


conn.commit()  #commit the changes

conn.close()  # close the connection
