import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("price",
        type=float,
        required= True,
        help="This field cannot be left blank"
    )
    
    @jwt_required()
    def get(self, name):
        
        item = ItemModel.find_by_name(name)
    
        if item:
            return item.json()
        return {'message': 'Item not found'}, 404
        #return {'item': next(filter(lambda x: x["name"] == name, items), None)}


  

    @jwt_required()
    def post(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return {'message': "An item with name '{}' already exists.".format(name)}

        data = Item.parser.parse_args()
        item = ItemModel(name, data["price"])

        try:
             item.insert_item()
        except:
            return {"message": "An Error Occured while inserting into the database"}, 500        
        return item.json, 201

    @jwt_required()
    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            connection = sqlite3.connect('data.db')
            cursor = connection.cursor()
            delt_query = "DELETE FROM items WHERE name=?"
            cursor.execute(delt_query, (name,))
            connection.commit()
            connection.close()
            return "deleted successfully",200
        return "No item found to delete", 404


    def put(self, name):
        #get_data = request.get_json()
        #request parser takes the requested data body

        get_data = self.parser.parse_args()

        update_item = ItemModel(name, price)
#next() is used just like a break in an iterative loop...like below if the lambda function gets an item with x['name'] == name , then break and get out of  the loop and execute the next statement
        #get_item = next(filter(lambda x: x["name"] == name ,items), None)
        item = ItemModel.find_by_name(name)
        print("***********************************************************************8")
        print(item)

        if item is None:
            update_item.insert_item()
            return items
        else:
            print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
            print(update_item)
            update_item.updating_item()
            return "Item has been updated successfully"


class ItemList(Resource):
    def get(self):
        items = []
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM items"
        rows = cursor.execute(query)
        for row in rows:
            items.append({"name": row[0], "price": row[1]})
        connection.close()
        return{'items': items}

