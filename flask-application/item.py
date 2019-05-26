import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("price",
        type=float,
        required= True,
        help="This field cannot be left blank"
    )
    
    @jwt_required()
    def get(self, name):
        item = self.find_by_name(name)
    
        if item:
            return item
        return {'message': 'Item not found'}, 404
        #return {'item': next(filter(lambda x: x["name"] == name, items), None)}


    @classmethod
    def find_by_name(cls,name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM items WHERE name=?"
        result = cursor.execute(query,(name,))
        row = result.fetchone()
        connection.close()

        if row:
            return {'item': {'name': row[0], 'price': row[1]}}

    @classmethod
    def insert_item(cls,item):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "INSERT INTO items VALUES(?, ?)"
        cursor.execute(query, (item["name"], item["price"]))
        connection.commit()
        connection.close()



    @jwt_required()
    def post(self, name):
        item = self.find_by_name(name)
        if item:
            return {'message': "An item with name '{}' already exists.".format(name)}

        data = Item.parser.parse_args()
        item = {"name": name, "price": data["price"]}

        try:
            self.insert_item(item)
        except:
            return {"message": "An Error Occured while inserting into the database"}, 500        
        return item, 201

    @jwt_required()
    def delete(self, name):
        item = self.find_by_name(name)
        if item:
            connection = sqlite3.connect('data.db')
            cursor = connection.cursor()
            delt_query = "DELETE FROM items WHERE name=?"
            cursor.execute(delt_query, (name,))
            connection.commit()
            connection.close()
            return "deleted successfully",200
        return "No item found to delete", 404
    @classmethod
    def updating_item(cls,item):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        update_query = "UPDATE items SET price=? WHERE name =?"
        cursor.execute(update_query, (item["price"], item["name"]))
        connection.commit()
        connection.close()

    def put(self, name):
        #get_data = request.get_json()
        #request parser takes the requested data body

        get_data = self.parser.parse_args()

        update_item = {"name": name, "price": get_data["price"]}
#next() is used just like a break in an iterative loop...like below if the lambda function gets an item with x['name'] == name , then break and get out of  the loop and execute the next statement
        #get_item = next(filter(lambda x: x["name"] == name ,items), None)
        item = self.find_by_name(name)
        print("***********************************************************************8")
        print(item)

        if item is None:
            self.insert_item(update_item)
            return items
        else:
            print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
            print(update_item)
            self.updating_item(update_item)
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

