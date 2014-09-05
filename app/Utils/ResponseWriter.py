from flask import render_template,json,jsonify,Response
from bson import BSON
from bson import json_util
import json
from bson.json_util import dumps

def write_response(data):
	resp = Response(dumps(data,default=json_util.default),200,mimetype='application/json')
	return resp
def format(data):
	resp = json.loads(data)
	return resp
def write_error_response(code,message):
	resp = Response(dumps(message),code,mimetype='application/json')
	return resp