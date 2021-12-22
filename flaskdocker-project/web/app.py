from flask import Flask, request
from flask_restful import Resource, Api
from pymongo import MongoClient


# Init Flask and API
app = Flask(__name__)
api = Api(app)

#->> initialize a new client:
# db is the name of the folder that have the Dockerfile of mongoDB
# default port used by mongoDB: 27017
client = MongoClient("mongodb://db:27017")
db = client["aNewDB"]                              # create a new DB named as aNewDB
UserNum = db["UserNum"]                         # create a collection

UserNum.insert_one({"num_of_users":0})

class Visit(Resource):
    def get(self):
        prev_num = UserNum.find({})[0]["num_of_users"]
        new_num = prev_num+1

        #update db
        UserNum.update_one({}, {'$set': {'num_of_users':new_num}})
        return "Hello user number "+ str(new_num)

# Resource
class Operation(Resource):
    def post(self):
        data = request.get_json()
        # Check to see if all vals are present
        if ('x' not in data) or ('y' not in data) or ('operation' not in data):
            return "Please enter all values", 301

        # Check operation type and data values
        
        operation = data['operation'].lower()
        res = 0

        if operation in ['add', 'subtract', 'divide', 'multiply']:
            x,y = data['x'], data['y']
        else:
            return "Please enter a valid operation"


        # if div denominator cannot be 0
        if operation == 'division':
            if y == 0:
                return 'Denominator cannot be equal to zero!', 400

        # compute
        if operation == 'add':
            res = x+y
        if operation == 'subtract':
            res = x-y
        if operation == 'multiply':
            res = x*y
        if operation == 'divide':
            res = x/y
        
        return {'Computed Result': res}


# Setup links and run!        
api.add_resource(Operation, '/calc')
api.add_resource(Visit, '/')
app.run(host="0.0.0.0", port="3000", debug=True)

