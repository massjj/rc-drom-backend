from flask import Flask, jsonify,request,render_template
from flask_cors import CORS, cross_origin
from src.Userlogin import *
from src.Status import *
from src.Repairlist import *
from src.Itemlist import *
from src.Maintenance import *

app = Flask(__name__)
cors = CORS(app)
userlogins = Userlogin()
status = Status()
repairlists = Repairlist()
itemlists = Itemlist()
maintenances = Maintenance()

@app.route('/')
@cross_origin()
def home():
    print(os.getenv("DB_HOST"))
    return "Welcom to backend EiEi"

#Userlogin
@app.route('/getUserlogin', methods=['GET'])
@cross_origin()
def getUserlogin():
    x = userlogins.dump()
    return jsonify(x)

@app.route('/readUserlogin', methods=['GET'])
@cross_origin()
def readUserlogin():
   if request.method=='GET':
      userId=request.form['user_id']
      logs = userlogins.read(userId)
      return jsonify(logs)
   else:
      return "Please use post medthod"

@app.route('/createUserlogin',methods=['POST'])
@cross_origin()
def createUserlogin():
   if request.method=='POST':
      userId=request.form['user_id']
      password=request.form['password']
      userType=request.form['user_type']
      userName=request.form['user_name']
      logs = userlogins.create(userId, password, userType, userName)
      return jsonify(logs)
   else:
      return "Please use post medthod"

@app.route('/updateUserlogin',methods=['PUT'])
@cross_origin()
def updateUserlogin():
   if request.method=='PUT':
      userId=request.form['user_id']
      newpassword=request.form['password']
      newuserType=request.form['user_type']
      newuserName=request.form['user_name']
      logs = userlogins.update(userId, newpassword, newuserType, newuserName)
      return jsonify(logs)
   else:
      return "Please use post medthod"

@app.route('/deleteUserlogin', methods=['DELETE'])
@cross_origin()
def deleteUserlogin():
   if request.method=='DELETE':
      userId=request.form['user_id']
      logs = userlogins.delete(userId)
      return jsonify(logs)
   else:
      return "Please use post medthod"

#Status
@app.route('/getStatus', methods=['GET'])
@cross_origin()
def getStatus():
    x = status.dump()
    return jsonify(x)

@app.route('/readStatus', methods=['GET'])
@cross_origin()
def readStatus():
   if request.method=='GET':
      statusId=request.form['status_id']
      logs = status.read(statusId)
      return jsonify(logs)
   else:
      return "Please use post medthod"

@app.route('/createStatus',methods=['POST'])
@cross_origin()
def createStatus():
   if request.method=='POST':
      statusId=request.form['status_id']
      statusName=request.form['status_name']
      logs = status.create(statusId, statusName)
      return jsonify(logs)
   else:
      return "Please use post medthod"

@app.route('/updateStatus',methods=['PUT'])
@cross_origin()
def updateStatus():
   if request.method=='PUT':
      statusId=request.form['status_id']
      newstatusName=request.form['status_name']
      logs = status.update(statusId, newstatusName)
      return jsonify(logs)
   else:
      return "Please use post medthod"

@app.route('/deleteStatus', methods=['DELETE'])
@cross_origin()
def deleteStatus():
   if request.method=='DELETE':
      statusId=request.form['status_id']
      logs = status.delete(statusId)
      return jsonify(logs)
   else:
      return "Please use post medthod"

#Repairlist
@app.route('/getRepairlist', methods=['GET'])
@cross_origin()
def getRepairlist():
    x = repairlists.dump()
    return jsonify(x)

@app.route('/readRepairlist', methods=['GET'])
@cross_origin()
def readRepairlist():
   if request.method=='GET':
      repairId=request.form['repair_id']
      logs = repairlists.readrepairlist(repairId)
      return jsonify(logs)
   else:
      return "Please use post medthod"

@app.route('/createRepairlist',methods=['POST'])
@cross_origin()
def createRepairlist():
   if request.method=='POST':
      # repairId=request.form['repair_id']
      userId=request.form['user_id']
      statusId=request.form['status_id']
      maintenanceId=request.form['maintenance_id']
      phone=request.form['phone']
      informDate=request.form['inform_date']
      acceptDate=request.form['accept_date']
      repairDate=request.form['repair_date']
      timeRepair=request.form['time_repair']
      description=request.form['description']
      logs = repairlists.register(userId,statusId,maintenanceId,phone,informDate,acceptDate,repairDate,timeRepair,description)
      return jsonify(logs)
   else:
      return "Please use post medthod"

@app.route('/updateRepairlist',methods=['PUT'])
@cross_origin()
def updateRepairlist():
   if request.method=='PUT':
      repairId=request.form['repair_id']
      newuserId=request.form['user_id']
      newstatusId=request.form['status_id']
      newmaintenanceId=request.form['maintenance_id']
      newphone=request.form['phone']
      newinformDate=request.form['inform_date']
      newacceptDate=request.form['accept_date']
      newrepairDate=request.form['repair_date']
      newtimeRepair=request.form['time_repair']
      newdescription=request.form['description']
      logs = repairlists.update(repairId,newuserId,newstatusId,newmaintenanceId,newphone,newinformDate,newacceptDate,newrepairDate,newtimeRepair,newdescription)
      return jsonify(logs)
   else:
      return "Please use post medthod"

@app.route('/deleteRepairlist', methods=['DELETE'])
@cross_origin()
def deleteRepairlist():
   if request.method=='DELETE':
      repairId=request.form['repair_id']
      logs = repairlists.delete(repairId)
      return jsonify(logs)
   else:
      return "Please use post medthod"

@app.route('/readRepairlistitem', methods=['GET'])
@cross_origin()
def readRepairlistitem():
   if request.method=='GET':
      repairId=request.form['repair_id']
      itemId = request.form['item_id']
      logs = repairlists.readrepairlistitem(repairId,itemId)
      return jsonify(logs)
   else:
      return "Please use post medthod"

@app.route('/createRepairlistitem',methods=['POST'])
@cross_origin()
def createRepairlistitem():
   if request.method=='POST':
      repairId=request.form['repair_id']
      itemId = request.form['item_id']
      logs = repairlists.createLineItem(repairId,itemId)
      
      return jsonify(logs)
   else:
      return "Please use post medthod"

@app.route('/updateRepairlistitem',methods=['PUT'])
@cross_origin()
def updateRepairlistitem():
   if request.method=='PUT':
      repairId=request.form['repair_id']
      itemId = request.form['item_id']
      logs = repairlists.updatelineitem(repairId, itemId)
      
      return jsonify(logs)
   else:
      return "Please use post medthod"

@app.route('/deleteRepairlistitem', methods=['DELETE'])
@cross_origin()
def deleteRepairlistitem():
   if request.method=='DELETE':
      repairId=request.form['repair_id']
      itemId = request.form['item_id']
      logs = repairlists.deletelineitem(repairId,itemId)
      return jsonify(logs)

#Itemlist
@app.route('/getItemlist', methods=['GET'])
@cross_origin()
def getItemlist():
    x = itemlists.dump()
    return jsonify(x)

@app.route('/readItemlist', methods=['GET'])
def readItemlist():
   if request.method=='GET':
      itemId=request.form['item_id']
      logs = itemlists.read(itemId)
      return jsonify(logs)
   else:
      return "Please use post medthod"

@app.route('/createItemlist',methods=['POST'])
@cross_origin()
def createItemlist():
   if request.method=='POST':
      itemId=request.form['item_id']
      itemType=request.form['item_type']
      itemName=request.form['item_name']
      quantity=request.form['quantity']
      price=request.form['price']
      logs = itemlists.create(itemId, itemType, itemName, quantity, price)
      return jsonify(logs)
   else:
      return "Please use post medthod"

@app.route('/updateteItemlist',methods=['PUT'])
@cross_origin()
def updateteItemlist():
   if request.method=='PUT':
      itemId=request.form['item_id']
      newitemType=request.form['item_type']
      newitemName=request.form['item_name']
      newquantity=request.form['quantity']
      newprice=request.form['price']
      logs = itemlists.update(itemId, newitemType, newitemName, newquantity, newprice)
      return jsonify(logs)
   else:
      return "Please use post medthod"

@app.route('/deleteItemlist', methods=['DELETE'])
@cross_origin()
def deleteItemlist():
   if request.method=='DELETE':
      ItemId=request.form['item_id']
      logs = itemlists.delete(ItemId)
      return jsonify(logs)

#Maintenance
@app.route('/getMaintenance', methods=['GET'])
@cross_origin()
def getMaintenance():
    x = maintenances.dump()
    return jsonify(x)

@app.route('/readMaintenance', methods=['GET'])
@cross_origin()
def readMaintenance():
   if request.method=='GET':
      maintenanceId=request.form['maintenance_id']
      logs = maintenances.read(maintenanceId)
      return jsonify(logs)
   else:
      return "Please use post medthod"

@app.route('/createMaintenance',methods=['POST'])
@cross_origin()
def createMaintenance():
   if request.method=='POST':
      maintenanceId=request.form['maintenance_id']
      maintenanceName=request.form['maintenance_name']
      tel=request.form['tel']
      workingDate=request.form['working_date']
      workingTime=request.form['working_time']
      logs = maintenances.create(maintenanceId, maintenanceName, tel, workingDate,workingTime)
      return jsonify(logs)
   else:
      return "Please use post medthod"
    
@app.route('/updateMaintenance',methods=['PUT'])
@cross_origin()
def updateMaintenance():
   if request.method=='PUT':
      maintenanceId=request.form['maintenance_id']
      newmaintenanceName=request.form['maintenance_name']
      newtel=request.form['tel']
      newworkingDate=request.form['working_date']
      newworkingTime=request.form['working_time']
      logs = maintenances.update(maintenanceId, newmaintenanceName, newtel, newworkingDate,newworkingTime)
      return jsonify(logs)
   else:
      return "Please use post medthod"

@app.route('/deleteMaintenance', methods=['DELETE'])
@cross_origin()
def deleteMaintenance():
   if request.method=='DELETE':
      maintenanceId=request.form['maintenance_id']
      logs = maintenances.delete(maintenanceId)
      return jsonify(logs)

if __name__ == "__main__":
    app.run(debug=True)