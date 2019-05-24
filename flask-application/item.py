import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
class Item(Resource):
    @jwt_required()
    def get(self, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM items WHERE name=?"
        result = cursor.execute(query,(name,))
        row = result.fetchone()
        connection.close()

        if row:
            return {'item': {'name': row[0], 'price': row[1]}}
        return {'message': 'Item not found'}, 404
        #return {'item': next(filter(lambda x: x["name"] == name, items), None)}
        
    @jwt_required()
    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None):
            return {'message': "An item with name '{}' already exists.".format(name)}

        data = request.get_json()

        item = {"name": name, "price": data["price"]}
        items.append(item)
        return item, 201

    @jwt_required()
    def delete(self, name):
    	global items
    	items = list(filter(lambda x : x != name, items))
#to update a particular item
    def put(self, name):
        #get_data = request.get_json()
        #request parser takes the requested data body
        parser = reqparse.RequestParser()
        parser.add_argument("price",
            type=float,
            required= True,
            help="This field cannot be left blank"
           )
        get_data = parser.parse_args()
#next() is used just like a break in an iterative loop...like below if the lambda function gets an item with x['name'] == name , then break and get out of  the loop and execute the next statement
        get_item = next(filter(lambda x: x["name"] == name ,items), None)

        if get_item == None:
            items.append(get_data)
            return items
        else:
            get_item.update(get_data)
            return(get_item)
class ItemList(Resource):
    def get(self):
        return {'items': items}


