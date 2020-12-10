from src.DBHelper import *
from src.helper_functions import *
from src.Status import *
from src.Maintenance import *
from src.Userlogin import *
from src.Itemlist import *

class Repairlist:
    def __init__(self):
        self.db = DBHelper()
    
    def __updateRepairlistTotal (self, repairId):

        sql = ("UPDATE receipt SET "
               " total = line_item.total_repairlist"
               " FROM (SELECT repair_id, SUM(paid_amount) as total_repairlist FROM repair_item GROUP BY repair_id) line_item "
               " WHERE repairlist.repair_id = line_item.repair_id "
               " AND repairlist.repair_id = '{}' ".format(repairId))
        self.db.execute(sql)

    def __updateLineItem (self, repairId, repairLineTuplesList):
        self.db.execute ("DELETE FROM reapair_item WHERE repair_id = '{}' ".format(repairId))
        for lineItem in repairLineTuplesList:
            self.db.execute ("INSERT INTO repair_item (repair_id,user_id,item_id,amount_item,paid_amount,repair_date,description) VALUES ('{}','{}','{}','{}','{}','{}','{}')".format(repairId,lineItem["User ID"],lineItem["Item ID"],lineItem["Amount Item"],lineItem["Paid Amount"],lineItem["Repaid Date"],lineItem["Description"]))
        self.__updateRepairlistTotal(repairId)

    def create(self,  repairId, statusId, maintenanceId, phone,informDate,acceptrDate, repairLineTuplesList):
        data, columns = self.db.fetch ("SELECT * FROM repairlist WHERE repair_id = '{}' ".format(repairId))
        if len(data) > 0:
            return {'0.status': 'Error','1.Repair ID': '','2.Status ID' : '','3.Maintenance ID' : '','4.Phone' : '','5.Inform Date' : '','6.Accept Date' : '','7.Repair List' : ''}
        else:
            self.db.execute ("INSERT INTO repairlist (repair_id,status_id,maintenance_id,phone,inform_date,accept_date) VALUES ('{}' ,'{}','{}','{}','{}','{}')".format(repairId, statusId, maintenanceId, phone,informDate,acceptrDate))
            self.__updateLineItem(repairId,repairLineTuplesList)
        return {'0.status': 'Correct','1.Repair ID': '{}'.format(repairId),'2.Status ID' : '{}'.format(statusId),'3.Maintenance ID' : '{}'.format(maintenanceId),'4.Phone' : '{}'.format(phone),'5.Inform Date' : '{}'.format(informdate),'6.Accept Date' : '{}'.format(acceptrDate),'7.Repair List' : '{}' '{}' '{}' '{}' '{}' '{}'.format(userId , itemId,amountItem,paidAmount,repairDate,description)}

    def read(self, repairId):
        data, columns = self.db.fetch ("SELECT * FROM repairlist WHERE repair_id = '{}' ".format(repairId))
        if len(data) > 0:
            retRepairlist = row_as_dict(data, columns)
        else:
            return ({'Is Error': True, 'Error Message': "Repair ID '{}' not found. Cannot Read.".format(repairId)},{})
        return ({'Is Error': False, 'Error Message': ""},retRepairlist)

    def update(self, repairId, newStatusId, newMaintenanceId, newPhone,newInformDate,newAcceptrDate, newRepairLineTuplesList):
        data, columns = self.db.fetch ("SELECT * FROM repairlist WHERE repair_id = '{}' ".format(repairId))
        if len(data) > 0:
            self.db.execute ("UPDATE repairlist SET  status_id = '{}', maintanence_id = '{}', phone='{}',inform_date={},accept_date={} WHERE repair_id = '{}' ".format(newStatusId,newMaintenanceId,newPhone,newInformDate,newAcceptrDate,repairId))
            self.__updateLineItem(repairId, newRepairLineTuplesList)
        else:
            return {'Is Error': True, 'Error Message': "Repair ID '{}' not found. Cannot Update.".format(repairId)}
        return {'Is Error': False, 'Error Message': ""}

    def delete(self, repairId):
        data, columns = self.db.fetch ("SELECT * FROM repairlist WHERE repair_id = '{}' ".format(repairId))
        if len(data) > 0:
            self.db.execute ("DELETE FROM repairlist WHERE repair_id = '{}' ".format(repairId))
            self.db.execute ("DELETE FROM repair_item WHERE repair_id = '{}' ".format(repairId))
        else:
            return {'Is Error': True, 'Error Message': "Repair ID '{}' not found. Cannot Delete".format(repairId)}
        return {'Is Error': False, 'Error Message': ""}

    def dump(self):
        db = DBHelper()
        data, columns = db.fetch ('SELECT r.repair_id as "Repair ID", r.status_id as "Status ID",r.maintenance_id as "Maintenanace ID" '
                              ' , r.phone as "Phone", r.inform_date as "Inform Date",r.accept_date as "Accept Date" '
                              ' ,  r.total as "Total" '
                              ' , ri.user_id as "User ID", ri.item_id as "Item ID"'
                              ' , ri.amount_item As "Amount Item",ri.paid_amount as "Paid Amount",ri.repair_date as "Repair Date",ri.description as "Description"'
                              ' FROM repairlist r JOIN status s ON r.status_id = s.status_id '
                              '  JOIN maintenance m ON r.maintenance_id = m.maintenance_id'
                              '  JOIN repair_item ri ON r.repair_id = ri.repair_id '
                              '  JOIN userlogin u ON ri.user_id = u.user_id'
                              '  JOIN itemlist t ON ri.item_id = t.item_id '
                              ' ')
        return row_as_dict(data, columns)

    def update_repair_line(self, repairId, userId , itemId,amountItem,paidAmount,repairDate,description):
        data, columns = self.db.fetch ("SELECT * FROM repair_item WHERE repair_id = '{}' AND user_id = '{}' AND item_id = '{}' ".format(repairId, userId , itemId))
        if len(data) > 0:
            self.db.execute ("UPDATE repair_item SET amount_item = '{}',paid_amount = '{}', repair_date = {}, description = '{}' WHERE repair_id = '{}' AND user_id = '{}' AND item_id = '{}' ".format(amountItem,paidAmount,repairDate,description,repairId, userId , itemId))
            self.__updateRepairlistTotal(repairId)
        else:
            return {'Is Error': True, 'Error Message': "User ID '{}' not found in Repair ID '{}'. Cannot Update.".format(userId, repairId)}

        return {'Is Error': False, 'Error Message': ""}


    def delete_receipt_line(self,repairId, userId , itemId):
        data, columns = self.db.fetch ("SELECT * FROM repair_item WHERE repair_id = '{}' AND user_id = '{}' AND item_id = '{}' ".format(repairId, userId , itemId))
        if len(data) > 0:
            self.db.execute ("DELETE FROM repair_item WHERE  repair_id = '{}' AND user_id = '{}' AND item_id = '{}' ".format(repairId, userId , itemId))
            self.__updateRepairlistTotal(repairId)

        else:
            return {'Is Error': True, 'Error Message': "User ID '{}' not found in Repair ID '{}'. Cannot Update.".format(userId, repairId)}

        return {'Is Error': False, 'Error Message': ""}

