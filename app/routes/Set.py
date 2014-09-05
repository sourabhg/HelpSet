from app import app
from helpset.HelpSet import HelpSet
from app.Utils.ResponseWriter import write_response,format,write_error_response
from flask import request
from app.Utils.serverSets import server_sets


@app.route('/v1/helpshift/sets/create',methods=['POST'])
def createSet():
	if request.form.get('values') is not None:
		helpset = HelpSet(request.form.get('values').split(","))
	else:
		helpset = helpset()
	
	set_id = len(server_sets) + 1

	server_sets[set_id] = helpset

	return write_response({"set_id" : set_id,"values" : helpset.listSet()})

@app.route('/v1/helpshift/sets/delete/<int:set_id>',methods=['POST'])
def deleteSet(set_id):
	if server_sets.get(set_id) is not None:
		res = server_sets.get(set_id).delete()
		return write_response({"set_id" : set_id,"values" : res})
	else:
		return write_error_response('412',{"Error":"No Set Found"})

@app.route('/v1/helpshift/sets/display/<int:set_id>',methods=['GET'])
def displaySet(set_id):
	 print server_sets
	 if server_sets.get(set_id,None) != None:
	 	hs = server_sets.get(set_id)
	 	return write_response(hs.listSet())
	 else:
	 	return write_response({"Error":" No Set by such set id "})

@app.route('/v1/helpshift/sets/add/<int:set_id>',methods=['POST'])
def addMember(set_id):
	if request.form.get('member') is not None:
			res = server_sets.get(set_id).add(request.form.get('member'))
	else:
			return write_error_response('412',{"Error":"Parameter Member is mandatory"})
	
	return write_response(res)

@app.route('/v1/helpshift/sets/union/<int:set_id1>/<int:set_id2>',methods=['GET'])
def union(set_id1,set_id2):
	if server_sets.get(set_id1) is not None and server_sets.get(set_id2) is not None:
		union = server_sets.get(set_id1).union(server_sets.get(set_id2))
		print union
		return write_response(union)
	else:
		return write_error_response('412',{"Error":"Sets Not Present , First Create the sets"})

@app.route('/v1/helpshift/sets/intersect/<int:set_id1>/<int:set_id2>',methods=['GET'])
def intersect(set_id1,set_id2):
	if server_sets.get(set_id1) is not None and server_sets.get(set_id2) is not None:
		intersect = server_sets.get(set_id1).intersect(server_sets.get(set_id2))
		return write_response(intersect)
	else:
		return write_error_response('412',{"Error":"Sets Not Present , First Create the sets"})

@app.route('/v1/helpshift/sets/cardinality/<int:set_id>',methods=['GET'])
def getCardinality(set_id):
	if server_sets.get(set_id) is not None:
		return write_response(server_sets.get(set_id).cardinality())
	else:
		return write_error_response({"Error":"No Such set present"})

@app.route('/v1/helpshift/sets/remove/<int:set_id>/<member>',methods=['GET'])
def removeMember(set_id,member):
	if server_sets.get(set_id) is not None:
		res = server_sets.get(set_id).remove(member)
		return write_response(res)
	else:
		return write_error_response('412',{"Error":"No Such Set Present"})

@app.route('/v1/helpshift/sets/difference/<int:set_id1>/<int:set_id2>')
def getDifference(set_id1,set_id2):
	if server_sets.get(set_id1) is not None and server_sets.get(set_id2) is not None:
		difference = server_sets.get(set_id1).difference(server_sets.get(set_id2))
		return write_response(difference)
	else:
		return write_error_response('412',{"Error":"Sets Not Present , First Create the sets"})