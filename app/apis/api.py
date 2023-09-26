from app import app
from flask import request, jsonify
import json
from app.apis.crud import inserting, getData, getRedisCache, setRedisCache, delRedisCache

@app.route("/")
def index():
    return "connected to app server"

@app.route("/create", methods=['POST'])
def postDataToDb():
    payload = request.get_json()
    value = payload['data']
    if value:
        res = inserting(value)
        delRedisCache()
        if res:
            return jsonify({"message":'Data posted successfully'}), 201
    else:
        return jsonify({"message" : "Your field is empty"}), 400
    
@app.route("/data")
def getDatafromDB():
    data = []

    try:
        res = getRedisCache()
        if res:
            res = json.loads(res)
            return jsonify({'message' : 'success', 'isCached':'yes', 'data':res}), 200
        if res is None:
            res = getData()
            for i in res:
                data.append({'data':i.data})

            setRedisCache(json.dumps(data))
            return jsonify({'message' : 'success', 'isCached':'No', 'Data':data}), 200
    except:
        pass