from src.DBHelper import *
from src.helper_functions import *

class Status:
    def __init__(self):
        self.db = DBHelper()

    def create(self, statusId, statusName):
        data, columns = self.db.fetch ("SELECT * FROM status WHERE status_id = '{}' ".format(statusId))
        if len(data) > 0:
            return {'0.status': 'Error','1.Status ID': '','2.Status Name' : ''}
        else:
            self.db.execute ("INSERT INTO status (status_id,status_name) VALUES ('{}' ,'{}')".format(statusId,statusName))
        return {'0.status': 'Correct','1.Status ID': '{}'.format(statusId),'2.Status Name' : '{}'.format(statusName)}
    
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
            return {'0.status': 'Update Error','1.Status ID': '','2.Status Name' : ''}

        return {'0.status': 'Update Successful','1.Status ID': '{}'.format(statusId),'2.Status Name' : '{}'.format(newstatusName)}
    
    def delete(self, statusId):
        data, columns = self.db.fetch ("SELECT * FROM status WHERE status_id = '{}' ".format(statusId))
        if len(data) > 0:
            self.db.execute ("DELETE FROM status WHERE status_id='{}' ".format(statusId))
        else:
            return {'0.status': 'Delete Error','1.Status ID': ''}
        return {'0.status': 'Delete Succesful','1.Status ID': '{}'.format(statusId)}

    def dump(self):
        data, columns = self.db.fetch ('SELECT status_id as "Status_ID", status_name as "Status_Name" FROM status ')
        return row_as_dict(data, columns)
