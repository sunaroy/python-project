from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from security import authenticate, identity
from user import UserRegister

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True # To allow flask propagating exception even if debug is set to false on app
app.secret_key = 'jose'
api = Api(app)


jwt = JWT(app, authenticate, identity)

items = []

class Item(Resource):

    def get(self, name):
        for item in items:
            if item["name"] == name:
                return item
        return "no item found"
        #return {'item': next(filter(lambda x: x["name"] == name, items), None)}

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

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    app.run(debug=True)  # important to mention debug=True