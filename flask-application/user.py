import sqlite3
from flask_restful import Resource, reqparse


class User(object):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
    	connection = sqlite3.connect('data.db')
    	cursor = connection.cursor()


    	query = ("SELECT * FROM users WHERE username = ?")

    	row = cursor.execute(query, (username,))

    	if row:
    		print("********************88888888{}".format(row[1]))
    		user = cls(*row) #here cls is User
    	else:
    		user = none

    	connection.close()

    	return user

    @classmethod
    def find_by_id(cls, _id):
    	connection = sqlite3.connect('data.db')
    	cursor = connection.cursor()


    	query = ("SELECT * FROM users WHERE id = ?")

    	row = cursor.execute(query, (_id,))

    	if row:
    		user = cls(row[0], row[1], row[2]) #here cls is User
    	else:
    		user = none

    	connection.close()

    	return user




class UserRegister(Resource):
	parser = reqparse.RequestParser()
	parser.add_argument("username",
		type = str,							
		required=True,
		help="This field cannot be blank"
	)

	parser.add_argument("password",
		type=str,
		required=True,
		help="This field cannot be left blank"
	)

	def post(self):
		data = UserRegister.parser.parse_args()
		connection = sqlite3.connect('data.db')
		cursor = connection.cursor()

		insert_query = "INSERT INTO users VALUES(NULL, ?, ?)"

		cursor.execute(insert_query, (data["username"], data["password"]))
		connection.commit()
		connection.close()
		return {"message": "User created successfully"}, 201
