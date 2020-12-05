from src.DBHelper import *
from src.helper_functions import *

class Userlogin:
    def __init__(self):
        self.db = DBHelper()

    def create(self, userId, password, userType, userName):
        data, columns = self.db.fetch ("SELECT * FROM userlogin WHERE user_id = '{}' ".format(userId))
        if len(data) > 0:
            return {'Is Error': True, 'Error Message': "User ID '{}' already exists. Cannot Create. ".format(userId)}
        else:
            self.db.execute ("INSERT INTO userlogin (user_id,password,user_type,user_name) VALUES ('{}' ,'{}','{}','{}')".format(userId, password, userType, userName))
        return {'Is Error': False, 'Error Message': ""}

    def read(self, userId):
        data, columns = self.db.fetch ("SELECT user_id,password,user_type,user_name FROM userlogin WHERE user_id = '{}' ".format(userId))
        if len(data) > 0:
            retUserlogin = row_as_dict(data, columns)
        else:
            return ({'Is Error': True, 'Error Message': "User ID '{}' not found. Cannot Read.".format(userId)},{})

        return ({'Is Error': False, 'Error Message': ""},retUserlogin)

    def update(self, userId, newpassword, newuserType, newuserName):
        data, columns = self.db.fetch ("SELECT * FROM userlogin WHERE user_id = '{}' ".format(userId))
        if len(data) > 0:
            self.db.execute (" UPDATE userlogin SET password='{}',user_type='{}',user_name='{}' ".format(newpassword, newuserType, newuserName, userId))
        else:
            return {'Is Error': True, 'Error Message': "User ID '{}' not found. Cannot Update.".format(userId)}

        return {'Is Error': False, 'Error Message': ""}

    def delete(self, userId):
        data, columns = self.db.fetch ("SELECT * FROM userlogin WHERE user_id = '{}' ".format(userId))
        if len(data) > 0:
            self.db.execute ("DELETE FROM userlogin WHERE user_id='{}' ".format(userId))
        else:
            return {'Is Error': True, 'Error Message': "User ID '{}' not found. Cannot Delete".format(userId)}
        return {'Is Error': False, 'Error Message': ""}

    def dump(self):
        data, columns = self.db.fetch ('SELECT user_id as "User ID",password as "Password", user_type as "User Type", user_name as "User Name" FROM userlogin ')
        return row_as_dict(data, columns)