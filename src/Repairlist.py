from src.DBHelper import *
from src.helper_functions import *
from src.Status import *
from src.Maintenance import *
from src.Userlogin import *
from src.Itemlist import *

class Repairlist:
    def __init__(self):
        self.db = DBHelper()

    def create(self,  repairId,userId, phone,repairDate,timeRepair,description):
        self.db.execute ("INSERT INTO repairlist (repair_id,user_id,phone,repair_date,time_repair,description) VALUES ('{}','{}','{}','{}','{}','{}')".format(
            repairId,userId , phone,repairDate,timeRepair,description))
        return {'0.status': 'Correct','1.Repair ID': '{}'.format(repairId),'2.User ID' : '{}'.format(userId),
       '3.Phone' : '{}'.format(phone),'4.Repair Date' : '{}'.format(repairDate),'5.Time Repair' : '{}'.format(timeRepair),'6.Description' : '{}'.format(description)}

    def register(self, userId, phone,repairDate,timeRepair,description):
        data, columns = self.db.fetch ("SELECT MAX(r.repair_id) FROM repairlist r ")
        newID = increaseID(data[0][0],"RCT")
        logs = self.create(newID,userId, phone,repairDate,timeRepair,description)
        return logs

    def createLineItem (self, repairId, itemId):
        data,columns = self.db.fetch ("SELECT * FROM repair_item WHERE repair_id = '{}' AND item_id = '{}' ".format(repairId,itemId))
        if len(data) > 0:
            return {'0.status': 'Error','1.Repair ID': '','2.Item ID' : ''}
        else:
            self.db.execute ("INSERT INTO repair_item (repair_id,item_id) VALUES ('{}','{}')".format(repairId, itemId))
        return {'0.status': 'Correct','1.Repair ID': '{}'.format(repairId),'2.Item ID' : '{}'.format(itemId)}

    def registerlineitem(self, itemId):
        data, columns = self.db.fetch ("SELECT MAX(r.repair_id) FROM repair_item r ")
        newID = increaseID(data[0][0],"RCT")
        logs = self.createLineItem(newID,itemId)
        return logs

    def readrepairlist(self, repairId):
        data, columns = self.db.fetch ("SELECT * FROM repairlist WHERE repair_id = '{}'".format(repairId))
        if len(data) > 0:
            retRepairlist = row_as_dict(data, columns)
        else:
            return ({'Is Error': 'Error', 'Error Message': "Repair ID '{}' not found. Cannot Read.".format(repairId)},{})
        return ({'Is Error': 'Correct', 'Error Message': ""},retRepairlist)

    def readrepairlistitem(self, repairId,itemId):
        data, columns = self.db.fetch ("SELECT * FROM repair_item WHERE repair_id = '{}' AND item_id = '{}' ".format(repairId,itemId))
        if len(data) > 0:
            retRepairlist = row_as_dict(data, columns)
        else:
            return ({'Is Error': 'Error', 'Error Message': "Repair ID '{}' , Item ID '{}' not found. Cannot Read.".format(repairId,itemId)},{})
        return ({'Is Error': 'Correct', 'Error Message': ""},retRepairlist)

    def update(self, repairId,newuserId, newphone,newrepairDate,newtimeRepair,newdescription):
        data, columns = self.db.fetch ("SELECT * FROM repairlist WHERE repair_id = '{}' ".format(repairId))
        if len(data) > 0:
            self.db.execute("UPDATE repairlist SET user_id = '{}', phone='{}',repair_date = '{}',time_repair = '{}',description='{}' WHERE repair_id = '{}' ".format(newuserId,newphone,newrepairDate,newtimeRepair,newdescription,repairId))
        else:
            return {'0.status': 'Update Error','1.Repair ID': '','2.User ID':'','3.Phone' : '','4.Repair Date' : '','5.Time Repair' : '','6.Description' : ''}
        return {'0.status': 'Update Successful','1.Repair ID': '{}'.format(repairId),'2.User ID' : '{}'.format(newuserId),'3.Phone' : '{}'.format(newphone),'4.Repair Date' : '{}'.format(newrepairDate),'5.Time Repair' : '{}'.format(newtimeRepair),'6.Description' : '{}'.format(newdescription)}

    def updatelineitem(self, repairId , itemId):
        data, columns = self.db.fetch ("SELECT * FROM repair_item WHERE repair_id = '{}' AND item_id = '{}' ".format(repairId,itemId))
        if len(data) > 0:
            self.db.execute ("UPDATE repair_item WHERE repair_id = '{}' AND item_id = '{}'".format(repairId,itemId))
        else:
            return {'0.status': 'Update Error','1.Repair ID': '','2.Item ID' : ''}
        return {'0.status': 'Update Succesful','1.Repair ID': '{}'.format(repairId),'2.Item ID' : '{}'.format(itemId)}

    
    def delete(self, repairId):
        data, columns = self.db.fetch ("SELECT * FROM repairlist WHERE repair_id = '{}' ".format(repairId))
        if len(data) > 0:
            self.db.execute ("DELETE FROM repairlist WHERE repair_id = '{}' ".format(repairId))
        else:
            return {'0.status': 'Delete Error','1.Repair ID': ''}
        return {'0.status': 'Delete Succesful','1.Repair ID': '{}'.format(repairId)}

    def deletelineitem(self, repairId,itemId):
        data, columns = self.db.fetch ("SELECT * FROM repair_item WHERE repair_id = '{}' AND item_id = '{}' ".format(repairId,itemId))
        if len(data) > 0:
            self.db.execute ("DELETE FROM repair_item WHERE repair_id = '{}' AND itemId = '{}' ".format(repairId,itemId))
        else:
            return {'0.status': 'Delete Error','1.Repair ID': ''}
        return {'0.status': 'Delete Succesful','1.Repair ID': '{}'.format(repairId),'2.Item ID' : '{}'.format(itemId)}

    def dump(self):
        db = DBHelper()
        data, columns = db.fetch ('SELECT r.repair_id as "Repair ID", r.user_id as "User ID" '
                              ' , r.phone as "Phone",r.time_repair as "Time Repair" '
                              ' , r.description as "Description" '
                              ' , ri.item_id as "Item ID"'
                              ' , r.repair_date as "Repair Date"'
                              ' FROM repairlist r JOIN userlogin u ON r.user_id = u.user_id  '
                              '  JOIN repair_item ri ON r.repair_id = ri.repair_id '
                              ' ')
        return row_as_dict(data, columns)

