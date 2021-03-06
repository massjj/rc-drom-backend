from src.DBHelper import *
from src.helper_functions import *

class Status:
    def __init__(self):
        self.db = DBHelper()

    def create(self, statusId, statusName):
        data, columns = self.db.fetch ("SELECT * FROM status WHERE status_id = '{}' ".format(statusId))
        if len(data) > 0:
            return {'Is Error': True, 'Error Message': "Status ID '{}' already exists. Cannot Create. ".format(statusId)}
        else:
            self.db.execute ("INSERT INTO status (status_id,status_name) VALUES ('{}' ,'{}')".format(statusId,statusName))
        return {'Is Error': False, 'Error Message': ""}
    
    def read(self, statusId):
        data, columns = self.db.fetch ("SELECT status_id, status_name FROM status WHERE status_id = '{}' ".format(statusId))
        if len(data) > 0:
            retStatus = row_as_dict(data, columns)
        else:
            return ({'Is Error': True, 'Error Message': "Status ID '{}' not found. Cannot Read.".format(statusId)},{})

        return ({'Is Error': False, 'Error Message': ""},retStatus)
    
    def update(self, statusId, newstatusName):
        data, columns = self.db.fetch ("SELECT * FROM status WHERE status_id = '{}' ".format(statusId))
        if len(data) > 0:
            self.db.execute ("UPDATE status SET status_name='{}' WHERE status_id='{}' ".format(newstatusName, statusId))
        else:
            return {'Is Error': True, 'Error Message': "Status ID '{}' not found. Cannot Update.".format(statusId)}

        return {'Is Error': False, 'Error Message': ""}
    
    def delete(self, statusId):
        data, columns = self.db.fetch ("SELECT * FROM status WHERE status_id = '{}' ".format(statusId))
        if len(data) > 0:
            self.db.execute ("DELETE FROM status WHERE status_id='{}' ".format(statusId))
        else:
            return {'Is Error': True, 'Error Message': "Status ID '{}' not found. Cannot Delete".format(statusId)}
        return {'Is Error': False, 'Error Message': ""}

    def dump(self):
        data, columns = self.db.fetch ('SELECT status_id as "Status_ID", status_name as "Status_Name" FROM status ')
        return row_as_dict(data, columns)
