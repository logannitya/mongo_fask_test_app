import flask
from flask import request, jsonify
from flask_cors import CORS
import json
from pymongo import MongoClient
from bson.json_util import dumps


app = flask.Flask(__name__)
CORS(app)
app.config["DEBUG"] = True


try:
    mongoNityadbUser = MongoClient("mongodb://nitya:test1234@mongo-svc:5050/nityadb")
    
except:
    exit("Error: Unable to connect to the databases")

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive old version</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''


@app.route('/api/v1/resources/users/all', methods=['GET'])
def api_all():
   cursor = mongoNityadbUser.db.user.find()
   list_cur = list(cursor)
   return dumps(list_cur)



app.run(host='0.0.0.0')
   
