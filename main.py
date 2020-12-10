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
      userName=request.form['user_name']
      userType=request.form['user_type']
      logs = userlogins.create(userId, password, userType, userName)
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

#Repairlist
@app.route('/getRepairlist', methods=['GET'])
def getRepairlist():
    x = repairlists.dump()
    print(x)
    return jsonify(x)

@app.route('/createRepairlistitem',methods=['POST'])
def createRepairlistitem():
   if request.method=='POST':
      repairlists.execute ("DELETE FROM reapair_item WHERE repair_id = '{}' ".format(repairId))
      repairId=request.form['repair_id']
      userId = request.form['user_id']
      itemId = request.form['item_id']
      amountItem=request.form['amount_item']
      paidAmount=request.form['paid_amount']
      repairDate=request.form['repair_date']
      description=request.form['description']
      log = repairlists.create(repairId, userId , itemId,amountItem,paidAmount,repairDate,description)
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
      userId = request.form['user_id']
      itemId = request.form['item_id']
      amountItem=request.form['amount_item']
      paidAmount=request.form['paid_amount']
      repairDate=request.form['repair_date']
      description=request.form['description']
      repairLineTuplesList = ("INSERT INTO repair_item (repair_id,user_id,item_id,amount_item,paid_amount,repair_date,description) VALUES ('{}','{}','{}','{}','{}','{}','{}')".format(repairId, userId , itemId,amountItem,paidAmount,repairDate,description))
      # for repairLineTuplesList in repairLineTuplesList['repairLineTuplesList']:
      #    repairId = repairLineTuplesList['repair_id']
      #    userId = repairLineTuplesList['user_id']
      #    itemId = repairLineTuplesList['item_id']
      #    amountItem=repairLineTuplesList['amount_item']
      #    paidAmount=repairLineTuplesList['paid_amount']
      #    repairDate=repairLineTuplesList['repair_date']
      #    description=repairLineTuplesList['description']
      logs = repairlists.create(repairId,statusId,maintenanceId,phone,informDate,acceptDate,repairLineTuplesList)
    #   ,userId , itemId,amountItem,paidAmount,repairDate,description)
      return logs
   else:
      return "Please use post medthod"


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
    
if __name__ == "__main__":
    app.run(debug=True)