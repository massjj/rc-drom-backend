from src.DBHelper import *
from src.helper_functions import *
from src.Status import *
from src.Maintenance import *

class Repairlist:
    def __init__(self):
        self.db = DBHelper()
    
    def __updateRepairlistTotal (self, repairId):
        sql = ("UPDATE repairlist SET "
              "  total = line_item.new_total "
              " FROM (SELECT repair_id, SUM(price) as new_total FROM repair_item GROUP BY repair_id) line_item "
              " WHERE repairlist.repair_id = line_item.repair_id "
              " AND repairlist.repair_id = '{}' ".format(repairId))
        self.db.execute (sql)

    def __updateLineItem (self, repairId, repairLineTuplesList):
        self.db.execute ("DELETE FROM repair_item WHERE repair_id = '{}' ".format(repairId))
        for lineItem in repairLineTuplesList:
            self.db.execute ("INSERT INTO repair_item (repair_id,user_id,item_id,amount_item,paid_amount,repair_date,description) VALUES ('{}','{}','{}','{}','{}',{},'{}')".format(repairId,lineItem["User ID"],lineItem["Item ID"],lineItem["Amount Item"],lineItem["Paid Amount"],lineItem["Repaid Date"],lineItem["Description"]))
        self.__updateRepairlistTotal(repairId)

    def create(self, repairId, statusId, maintenanceId, phone,imformDate,acceptrDate, repairLineTuplesList):
        data, columns = self.db.fetch ("SELECT * FROM repairlist WHERE repair_id = '{}' ".format(repairId))
        if len(data) > 0:
            return {'Is Error': True, 'Error Message': "Repair ID '{}' already exists. Cannot Create. ".format(repairId)}
        else:
            self.db.execute ("INSERT INTO repairlist (repair_id,status_id,maintenance_id,phone,inform_date,accept_date) VALUES ('{}' ,'{}','{}','{}',{},{})".format(repairId, statusId, maintenanceId, phone,imformDate,acceptrDate))
            self.__updateLineItem(repairId, repairLineTuplesList)

        return {'Is Error': False, 'Error Message': ""}

    def read(self, repairId):
        data, columns = self.db.fetch ("SELECT repair_id,status_id,maintenanace_id,phone,inform_date,accept_date,total FROM repairlist WHERE repair_id = '{}' ".format(repairId))
        if len(data) > 0:
            retRepairlist = row_as_dict(data, columns)
        else:
            return ({'Is Error': True, 'Error Message': "Repair ID '{}' not found. Cannot Read.".format(repairId)},{})

        return ({'Is Error': False, 'Error Message': ""},retRepairlist)

    def update(self, repairId, newStatusId, newMaintenanceId, newPhone,newImformDate,newAcceptrDate, newRepairLineTuplesList):
        data, columns = self.db.fetch ("SELECT * FROM repairlist WHERE repair_id = '{}' ".format(repairId))
        if len(data) > 0:
            self.db.execute ("UPDATE repairlist SET status_id = '{}', maintanence_id = '{}', phone='{}',inform_date={},accept_date={} WHERE repair_id = '{}' ".format(newStatusId, newMaintenanceId, newPhone,newImformDate,newAcceptrDate,repairId))
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
        db = DBHelper
        data, columns = db.fetch ('SELECT r.repair_id as "Repair ID", r.status_id as "Status ID", r.maintenance_id as "Maintenance ID" '
                              ' , r.phone as "Phone", r.inform_date as "Inform Date",r.accept_date as "Accept Date", r.total as "Total"'
                              ' , ri.user_id as "User ID", ri.item_id as "Item ID" '
                              ' , ri.amount_item as "Amount Item", ri.paid_amount as "Paid Amount", ri.repair_date as "Repair Date", ri.description as "Description" '
                              ' FROM repairlist r JOIN status s ON r.status_id = s.status_id '
                              '  JOIN maintenance m ON r.maintenance_id = m.maintenance_id'
                              '  JOIN repair_item ri ON r.repair_id = ri.repair_id '
                              '  JOIN userlogin u ON ri.user_id = u.user_id '
                              '  JOIN itemlist t ON ri.item_id = t.item_id'
                              ' ')
        return row_as_dict(data, columns)

    def update_repairlist_line(self, repairId, userId,itemId,amountItem,paidAmount,repairDate,description): 
        data, columns = self.db.fetch ("SELECT * FROM repair_item WHERE repair_id = '{}' AND user_id = '{}' AND item_id = '{}' ".format(repairId, userId,itemId))
        if len(data) > 0:
            self.db.execute ("UPDATE repair_item SET amount_item = '{}', paid_amount = '{}', repair_date={}, decription ='{}' WHERE repair_id = '{}' AND user_id = '{}' AND item_id = '{}' ".format(amountItem,paidAmount,repairDate,description, repairId, userId,itemId))
            self.__updateRepairlistTotal(repairId)
        else:
            return {'Is Error': True, 'Error Message': "User ID '{}' AND Item ID '{}' not found in Repair ID '{}'. Cannot Update.".format(userId,itemId, repairId)}

        return {'Is Error': False, 'Error Message': ""}

    def delete_invoice_line(self, repairId, userId,itemId):
        data, columns = self.db.fetch ("SELECT * FROM repair_item WHERE repair_id = '{}' AND user_id = '{}' AND item_id = '{}' ".format(repairId, userId,itemId))
        if len(data) > 0:
            self.db.execute ("DELETE FROM repair_item WHERE repair_id = '{}' AND user_id = '{}' AND item_id = '{}' ".format(repairId, userId,itemId))
            self.__updateRepairlistTotal(repairId)

        else:
            return {'Is Error': True, 'Error Message': "User ID '{}' AND Item ID '{}' not found in Repair ID '{}'. Cannot Update.".format(userId,itemId, repairId)}

        return {'Is Error': False, 'Error Message': ""}

