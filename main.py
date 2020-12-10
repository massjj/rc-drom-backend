from flask import Flask, jsonify,request,render_template
from flask_cors import CORS
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
def home():
    print(os.getenv("DB_HOST"))
    return "Welcom to backend EiEi"

#Userlogin
@app.route('/getUserlogin', methods=['GET'])
def getUserlogin():
    x = userlogins.dump()
    return jsonify(x)

@app.route('/createUserlogin',methods=['POST'])
def createUserlogin():
   if request.method=='POST':
      userId=request.form['user_id']
      password=request.form['password']
      userType=request.form['user_type']
      userName=request.form['user_name']
      logs = userlogins.create(userId, password, userType, userName)
      return logs
   else:
      return "Please use post medthod"

@app.route('/updateUserlogin',methods=['PUT'])
def updateUserlogin():
   if request.method=='PUT':
      userId=request.form['user_id']
      newpassword=request.form['password']
      newuserType=request.form['user_type']
      newuserName=request.form['user_name']
      logs = userlogins.update(userId, newpassword, newuserType, newuserName)
      return logs
   else:
      return "Please use post medthod"

@app.route('/deleteUserlogin', methods=['DELETE'])
def deleteUserlogin():
   if request.method=='DELETE':
      userId=request.form['user_id']
      logs = userlogins.delete(userId)
      return logs
   else:
      return "Please use post medthod"

#Status
@app.route('/getStatus', methods=['GET'])
def getStatus():
    x = status.dump()
    return jsonify(x)

@app.route('/createStatus',methods=['POST'])
def createStatus():
   if request.method=='POST':
      statusId=request.form['status_id']
      statusName=request.form['status_name']
      logs = status.create(statusId, statusName)
      return logs
   else:
      return "Please use post medthod"

@app.route('/updateStatus',methods=['PUT'])
def updateStatus():
   if request.method=='PUT':
      statusId=request.form['status_id']
      newstatusName=request.form['status_name']
      logs = status.update(statusId, newstatusName)
      return logs
   else:
      return "Please use post medthod"

@app.route('/deleteStatus', methods=['DELETE'])
def deleteStatus():
   if request.method=='DELETE':
      statusId=request.form['status_id']
      logs = status.delete(statusId)
      return logs
   else:
      return "Please use post medthod"

#Repairlist
@app.route('/getRepairlist', methods=['GET'])
def getRepairlist():
    x = repairlists.dump()
    print(x)
    return jsonify(x)

@app.route('/createRepairlistitem',methods=['POST'])
def createRepairlistitem():
   if request.method=='POST':
      repairId=request.form['repair_id']
      userId = request.form['user_id']
      itemId = request.form['item_id']
      amountItem=request.form['amount_item']
      paidAmount=request.form['paid_amount']
      repairDate=request.form['repair_date']
      description=request.form['description']
      logs = repairlists.createLineItem(repairId,userId , itemId,amountItem,paidAmount,repairDate,description)
      
      return logs
   else:
      return "Please use post medthod"

@app.route('/updateRepairlistitem',methods=['PUT'])
def updateRepairlistitem():
   if request.method=='PUT':
      repairId=request.form['repair_id']
      newuserId = request.form['user_id']
      newitemId = request.form['item_id']
      newamountItem=request.form['amount_item']
      newpaidAmount=request.form['paid_amount']
      newrepairDate=request.form['repair_date']
      newdescription=request.form['description']
      logs = repairlists.updatelineitem(repairId,newuserId , newitemId,newamountItem,newpaidAmount,newrepairDate,newdescription)
      
      return logs
   else:
      return "Please use post medthod"

@app.route('/createRepairlist',methods=['POST'])
def createRepairlist():
   if request.method=='POST':
      repairId=request.form['repair_id']
      statusId=request.form['status_id']
      maintenanceId=request.form['maintenance_id']
      phone=request.form['phone']
      informDate=request.form['inform_date']
      acceptDate=request.form['accept_date']
      logs = repairlists.create(repairId,statusId,maintenanceId,phone,informDate,acceptDate)
      return logs
   else:
      return "Please use post medthod"

@app.route('/updateRepairlist',methods=['PUT'])
def updateRepairlist():
   if request.method=='PUT':
      repairId=request.form['repair_id']
      newstatusId=request.form['status_id']
      newmaintenanceId=request.form['maintenance_id']
      newphone=request.form['phone']
      newinformDate=request.form['inform_date']
      newacceptDate=request.form['accept_date']
      logs = repairlists.update(repairId,newstatusId,newmaintenanceId,newphone,newinformDate,newacceptDate)
      return logs
   else:
      return "Please use post medthod"

@app.route('/deleteRepairlist', methods=['DELETE'])
def deleteRepairlist():
   if request.method=='DELETE':
      repairId=request.form['repair_id']
      logs = repairlists.delete(repairId)
      return logs
   else:
      return "Please use post medthod"

@app.route('/deleteRepairlistitem', methods=['DELETE'])
def deleteRepairlistitem():
   if request.method=='DELETE':
      repairId=request.form['repair_id']
      logs = repairlists.deletelineitem(repairId)
      return logs

#Itemlist
@app.route('/getItemlist', methods=['GET'])
def getItemlist():
    x = itemlists.dump()
    return jsonify(x)

@app.route('/createItemlist',methods=['POST'])
def createItemlist():
   if request.method=='POST':
      itemId=request.form['item_id']
      itemType=request.form['item_type']
      itemName=request.form['item_name']
      quantity=request.form['quantity']
      price=request.form['price']
      logs = itemlists.create(itemId, itemType, itemName, quantity, price)
      return logs
   else:
      return "Please use post medthod"

@app.route('/updateteItemlist',methods=['PUT'])
def updateteItemlist():
   if request.method=='PUT':
      itemId=request.form['item_id']
      newitemType=request.form['item_type']
      newitemName=request.form['item_name']
      newquantity=request.form['quantity']
      newprice=request.form['price']
      logs = itemlists.update(itemId, newitemType, newitemName, newquantity, newprice)
      return logs
   else:
      return "Please use post medthod"

@app.route('/deleteItemlist', methods=['DELETE'])
def deleteItemlist():
   if request.method=='DELETE':
      ItemId=request.form['item_id']
      logs = itemlists.delete(ItemId)
      return logs

#Maintenance
@app.route('/getMaintenance', methods=['GET'])
def getMaintenance():
    x = maintenances.dump()
    return jsonify(x)

@app.route('/createMaintenance',methods=['POST'])
def createMaintenance():
   if request.method=='POST':
      maintenanceId=request.form['maintenance_id']
      maintenanceName=request.form['maintenance_name']
      tel=request.form['tel']
      workingDate=request.form['working_date']
      workingTime=request.form['working_time']
      logs = maintenances.create(maintenanceId, maintenanceName, tel, workingDate,workingTime)
      return logs
   else:
      return "Please use post medthod"
    
@app.route('/updateMaintenance',methods=['PUT'])
def updateMaintenance():
   if request.method=='PUT':
      maintenanceId=request.form['maintenance_id']
      newmaintenanceName=request.form['maintenance_name']
      newtel=request.form['tel']
      newworkingDate=request.form['working_date']
      newworkingTime=request.form['working_time']
      logs = maintenances.update(maintenanceId, newmaintenanceName, newtel, newworkingDate,newworkingTime)
      return logs
   else:
      return "Please use post medthod"

@app.route('/deleteMaintenance', methods=['DELETE'])
def deleteMaintenance():
   if request.method=='DELETE':
      maintenanceId=request.form['maintenance_id']
      logs = maintenances.delete(maintenanceId)
      return logs

if __name__ == "__main__":
    app.run(debug=True)