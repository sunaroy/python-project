import sqlite3

#sqlite puts all data in a file type data base, here below sqlite3 creates a file named data.db where it is going to store data
connection = sqlite3.connect('data.db')

#cursor is responsible to run a query and store a result , it tells database from where to start to execute a query of db

cursor = connection.cursor()

create_table = "CREATE TABLE users(id int, username text, password text)"

cursor.execute(create_table)

user = (1, 'joe', 'asdf')

insert_query = "INSERT INTO users VALUES (?, ?, ?)"

cursor.execute(insert_query, user)


#insert multiple users

users = [
	(3, 'ross', 'yoyo'),
	(4, 'monica', 'mmm')
]
cursor.executemany(insert_query, users)


#get data from db

select_query = "SELECT * FROM users"

for row in cursor.execute(select_query):
	print('\n user is {}'.format(row))

connection.commit()

connection.close()