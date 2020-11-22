import flask
from flask import request, jsonify
from flask_cors import CORS
import json
from flask_pymongo import PyMongo

app = flask.Flask(__name__)
CORS(app)
app.config["DEBUG"] = True
app.config['MONGO_DBNAME'] = 'nityadb'
app.config['MONGO_URI'] = 'mongodb://nitya:test1234@mongo-svc:5050/nityadb'

mongo = PyMongo(app)



@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive old version</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''


@app.route('/api/v1/resources/users/all', methods=['GET'])
def api_all():
    users = mongo.db.user
    output= []
    for u in users.find():
        output.append({'EmpId' : u['EmpId'], 'EmpName' : u['EmpName']})
    return jsonify({'result' : output})



app.run(host='0.0.0.0')
   
