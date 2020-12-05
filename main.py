from flask import Flask, jsonify
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
    return "This is backend"

@app.route('/getUserlogin', methods=['GET'])
def getUserlogin():
    x = userlogins.dump()
    return jsonify(x)

@app.route('/getStatus', methods=['GET'])
def getStatus():
    x = status.dump()
    return jsonify(x)

@app.route('/getRepairlist', methods=['GET'])
def getRepairList():
    x = repairlists.dump()
    return jsonify(x)

@app.route('/getItemlist', methods=['GET'])
def getItemlist():
    x = itemlists.dump()
    return jsonify(x)

@app.route('/getMaintenance', methods=['GET'])
def getMaintenance():
    x = maintenances.dump()
    return jsonify(x)

    
if __name__ == "__main__":
    app.run(debug=True)