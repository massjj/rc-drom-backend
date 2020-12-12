from src.DBHelper import *
from src.helper_functions import *
from src.Status import *
from src.Maintenance import *
from src.Userlogin import *
from src.Itemlist import *

class Repairlist:
    def __init__(self):
        self.db = DBHelper()

    def create(self,  repairId,userId ,statusId, maintenanceId, phone,informDate,acceptDate,repairDate,timeRepair,description):
        self.db.execute ("INSERT INTO repairlist (repair_id,user_id,status_id,maintenance_id,phone,inform_date,accept_date,repair_date,time_repair,description) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(
            repairId,userId ,statusId, maintenanceId, phone,informDate,acceptDate,repairDate,timeRepair,description))
        return {'0.status': 'Correct','1.Repair ID': '{}'.format(repairId),'2.User ID' : '{}'.format(userId),'3.Status ID' : '{}'.format(statusId),
        '4.Maintenance ID' : '{}'.format(maintenanceId),'5.Phone' : '{}'.format(phone),'6.Inform Date' : '{}'.format(informDate),
        '7.Accept Date' : '{}'.format(acceptDate),'8.Repair Date' : '{}'.format(repairDate),'9.Time Repair' : '{}'.format(timeRepair),'10.Description' : '{}'.format(description)}

    def register(self, userId,statusId ,maintenanceId, phone,informDate,acceptDate,repairDate,timeRepair,description):
        data, columns = self.db.fetch ("SELECT MAX(r.repair_id) FROM repairlist r ")
        newID = increaseID(data[0][0],"RCT")
        logs = self.create(newID,userId ,statusId, maintenanceId, phone,informDate,acceptDate,repairDate,timeRepair,description)
        return logs

    def createLineItem (self, repairId, itemId):
        data,columns = self.db.fetch ("SELECT * FROM repair_item WHERE repair_id = '{}' AND item_id = '{}' ".format(repairId,itemId))
        if len(data) > 0:
            return {'0.status': 'Error','1.Repair ID': '','2.Item ID' : ''}
        else:
            self.db.execute ("INSERT INTO repair_item (repair_id,item_id) VALUES ('{}','{}')".format(repairId, itemId))
        return {'0.status': 'Correct','1.Repair ID': '{}'.format(repairId),'2.Item ID' : '{}'.format(itemId)}

    def registerlineitem(self, itemId,userId ,statusId, maintenanceId, phone,informDate,acceptDate,repairDate,timeRepair,description):
        data, columns = self.db.fetch ("SELECT MAX(r.repair_id) FROM repair_item r ")
        newID = increaseID(data[0][0],"RCT")
        logs = self.createLineItem(newID,itemId,userId ,statusId, maintenanceId, phone,informDate,acceptDate,repairDate,timeRepair,description)
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

    def update(self, repairId,newuserId, newstatusId, newmaintenanceId, newphone,newinformDate,newacceptDate,newrepairDate,newtimeRepair,newdescription):
        data, columns = self.db.fetch ("SELECT * FROM repairlist WHERE repair_id = '{}' ".format(repairId))
        if len(data) > 0:
            self.db.execute("UPDATE repairlist SET user_id = '{}',  status_id = '{}', maintenance_id = '{}', phone='{}',inform_date='{}',accept_date='{}',repair_date = '{}',time_repair = '{}',description='{}' WHERE repair_id = '{}' ".format(newuserId,newstatusId,newmaintenanceId,newphone,newinformDate,newacceptDate,newrepairDate,newtimeRepair,newdescription,repairId))
        else:
            return {'0.status': 'Update Error','1.Repair ID': '','2.User ID':'','3.Status ID' : '','4.Maintenance ID' : '','5.Phone' : '','6.Inform Date' : '','7.Accept Date' : '','8.Repair Date' : '','9.Time Repair' : '','10.Description' : ''}
        return {'0.status': 'Update Successful','1.Repair ID': '{}'.format(repairId),'2.User ID' : '{}'.format(newuserId),'3.Status ID' : '{}'.format(newstatusId),'4.Maintenance ID' : '{}'.format(newmaintenanceId),'5.Phone' : '{}'.format(newphone),'6.Inform Date' : '{}'.format(newinformDate),'7.Accept Date' : '{}'.format(newacceptDate),'8.Repair Date' : '{}'.format(newrepairDate),'9.Time Repair' : '{}'.format(newtimeRepair),'10.Description' : '{}'.format(newdescription)}

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
        data, columns = db.fetch ('SELECT r.repair_id as "Repair ID", r.user_id as "User ID", r.status_id as "Status ID",r.maintenance_id as "Maintenanace ID" '
                              ' , r.phone as "Phone", r.inform_date as "Inform Date",r.accept_date as "Accept Date",r.time_repair as "Time Repair" '
                              ' , r.description as "Description" '
                              ' , ri.item_id as "Item ID"'
                              ' , r.repair_date as "Repair Date"'
                              ' FROM repairlist r JOIN status s ON r.status_id = s.status_id '
                              '  JOIN maintenance m ON r.maintenance_id = m.maintenance_id'
                              '  JOIN repair_item ri ON r.repair_id = ri.repair_id '
                              '  JOIN userlogin u ON r.user_id = u.user_id'
                              '  JOIN itemlist t ON ri.item_id = t.item_id '
                              ' ')
        return row_as_dict(data, columns)

