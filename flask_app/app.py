from flask import Flask, request
from flask_restful import Resource, Api
app = Flask(__name__)
api = Api(app)

app.secret_key = 'jose'

items = []

class Item(Resource):
	def get(self,name):

		for item in items:
			if item['name'] == name:
				return item, 200
		return 'Not Found', 400



	def post(self, name):
		get_data = request.get_json()
		new_item = { "name": get_data["name"], "price": get_data["price"]}
		items.append(new_item)
		return new_item

api.add_resource(Item,'/item/<string:name>')

app.run(port=5000, debug=True)