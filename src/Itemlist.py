from src.DBHelper import *
from src.helper_functions import *

class Itemlist:
    def __init__(self):
        self.db = DBHelper()

    def create(self, itemId, itemType, itemName, quantity, price):
        data, columns = self.db.fetch ("SELECT * FROM itemlist WHERE item_id = '{}' ".format(itemId))
        if len(data) > 0:
            return {'0.status': 'Error','1.Item ID': '','2.Item Type' : '','3.Item Name' : '','4.Quantity' : '','5.Price' : ''}
        else:
            self.db.execute ("INSERT INTO itemlist (item_id,item_type,item_name,quantity,price) VALUES ('{}' ,'{}','{}','{}','{}')".format(itemId, itemType, itemName, quantity, price))
        return {'0.status': 'Correct','1.Item ID': '{}'.format(itemId),'2.Item Type' : '{}'.format(itemType),'3.Item Name' : '{}'.format(itemName),'4.Quantity' : '{}'.format(quantity),'5.Price' : '{}'.format(price)}

    def read(self, itemId):
        data, columns = self.db.fetch ("SELECT item_id,item_type,item_name,quantity,price FROM itemlist WHERE item_id = '{}' ".format(itemId))
        if len(data) > 0:
            retItemlist = row_as_dict(data, columns)
        else:
            return ({'Is Error': True, 'Error Message': "Item ID '{}' not found. Cannot Read.".format(itemId)},{})

        return ({'Is Error': False, 'Error Message': ""},retItemlist)

    def update(self, itemId, newitemType, newitemName, newQuantity, newPrice):
        data, columns = self.db.fetch ("SELECT * FROM itemlist WHERE item_id = '{}' ".format(itemId))
        if len(data) > 0:
            self.db.execute ("UPDATE itemlist SET item_type='{}',item_name='{}',quantity='{}',price='{}' WHERE item_id='{}' ".format(newitemType, newitemName, newQuantity, newPrice, itemId))
        else:
            return {'Is Error': True, 'Error Message': "Item ID '{}' not found. Cannot Update.".format(itemId)}

        return {'Is Error': False, 'Error Message': ""}

    def delete(self, itemId):
        data, columns = self.db.fetch ("SELECT * FROM itemlist WHERE item_id = '{}' ".format(itemId))
        if len(data) > 0:
            self.db.execute ("DELETE FROM itemlist WHERE item_id='{}' ".format(itemId))
        else:
            return {'Is Error': True, 'Error Message': "Item ID '{}' not found. Cannot Delete".format(itemId)}
        return {'Is Error': False, 'Error Message': ""}

    def dump(self):
        data, columns = self.db.fetch ('SELECT item_id as "Item ID",item_type as "Item Type", item_name as "Item Name", quantity as "Quantity", price as "Price" FROM itemlist ')
        return row_as_dict(data, columns)