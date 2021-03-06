from src.DBHelper import *
from src.helper_functions import *

class Maintenance:
    def __init__(self):
        self.db = DBHelper()

    def create(self, maintenanceId, maintenanceName, tel, workingDate,workingTime):
        data, columns = self.db.fetch ("SELECT * FROM maintenance WHERE maintenance_id = '{}' ".format(maintenanceId))
        if len(data) > 0:
            return {'Is Error': True, 'Error Message': "Maintenance ID '{}' already exists. Cannot Create. ".format(maintenanceId)}
        else:
            self.db.execute ("INSERT INTO maintenance (maintenance_id,maintenance_name,tel,working_date,working_time) VALUES ('{}' ,'{}','{}',{},{})".format(maintenanceId, maintenanceName, tel, workingDate,workingTime))
        return {'Is Error': False, 'Error Message': ""}

    def read(self, maintenanceId):
        data, columns = self.db.fetch ("SELECT maintenance_id,maintenance_name,tel,working_date,working_time FROM maintenance WHERE maintenance_id = '{}' ".format(maintenanceId))
        if len(data) > 0:
            retMaintenance = row_as_dict(data, columns)
        else:
            return ({'Is Error': True, 'Error Message': "Maintenance ID '{}' not found. Cannot Read.".format(maintenanceId)},{})

        return ({'Is Error': False, 'Error Message': ""},retMaintenance)

    def update(self, maintenanceId, newmaintenanceName, newtel, newworkingDate,newworkingTime):
        data, columns = self.db.fetch ("SELECT * FROM maintenance WHERE maintenance_id = '{}' ".format(maintenanceId))
        if len(data) > 0:
            self.db.execute (" UPDATE maintenance SET maintenance_name='{}',tel='{}',working_date= {} ,working_time = {} ".format(newmaintenanceName, newtel, newworkingDate,newworkingTime, maintenanceId))
        else:
            return {'Is Error': True, 'Error Message': "Maintenance ID '{}' not found. Cannot Update.".format(maintenanceId)}

        return {'Is Error': False, 'Error Message': ""}

    def delete(self, maintenanceId):
        data, columns = self.db.fetch ("SELECT * FROM maintenance WHERE maintenance_id = '{}' ".format(maintenanceId))
        if len(data) > 0:
            self.db.execute ("DELETE FROM maintenance WHERE maintenance_id='{}' ".format(maintenanceId))
        else:
            return {'Is Error': True, 'Error Message': "Maintenance ID '{}' not found. Cannot Delete".format(maintenanceId)}
        return {'Is Error': False, 'Error Message': ""}

    def dump(self):
        data, columns = self.db.fetch ('SELECT maintenance_id as "Maintenance ID", maintenance.maintanance_name as "Maintenance Name", tel as "Tel", working_date as "Working Date", working_time as "Working Time" '
                                        'FROM maintenance')
        return row_as_dict(data, columns)