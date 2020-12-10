from src.DBHelper import *
from src.helper_functions import *

class Userlogin:
    def __init__(self):
        self.db = DBHelper()

    def create(self, userId, password, userType, userName):
        data, columns = self.db.fetch ("SELECT * FROM userlogin WHERE user_id = '{}' ".format(userId))
        if len(data) > 0:
            return {'0.status': 'Error','1.User ID': '','2.Password' : '','3.User Type' : '','4.User Name' : ''}
        else:
            self.db.execute ("INSERT INTO userlogin (user_id,password,user_type,user_name) VALUES ('{}' ,'{}','{}','{}')".format(userId, password, userType, userName))
        return {'0.status': 'Correct','1.User ID': '{}'.format(userId),'2.Password' : '{}'.format(password),'3.User Type' : '{}'.format(userType),'4.User Name' : '{}'.format(userName)}

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
            self.db.execute (" UPDATE userlogin SET password ='{}',user_type = '{}', user_name = '{}' WHERE userlogin = '{}'".format(newpassword, newuserType, newuserName,userId))
        else:
            return {'Is Error': True, 'Error Message': "User ID '{}' not found. Cannot Update.".format(userId)}

        return {'Is Error': False, 'Error Message': ""}

    def delete(self, userId):
        data, columns = self.db.fetch ("SELECT * FROM userlogin WHERE user_id = '{}' ".format(userId))
        if len(data) > 0:
            self.db.execute ("DELETE FROM userlogin WHERE user_id='{}' ".format(userId))
        else:
            return {'Is Error': True, 'Error Message': "user ID '{}' not found. Cannot Delete".format(userId)}
        return {'Is Error': False, 'Error Message': ""}

    def dump(self):
        data, columns = self.db.fetch ('SELECT user_id as "User ID", password as "Password", user_type as "User Type", user_name as "User Name" '
                                        'FROM userlogin')
        return row_as_dict(data, columns)