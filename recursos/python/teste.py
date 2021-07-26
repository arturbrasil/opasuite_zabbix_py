# import sys
# from bson import ObjectId
import pymongo, json
from bson.json_util import dumps

database = pymongo.MongoClient("mongodb://127.0.0.1:27017/")["suite"]

data = {}

## usuarios
def getUsuarios():
    cursor = (database["usuarios"].find({"status": "A"}))
    list_cur = list(cursor)
    data_string = dumps(list_cur)
    data['usuarios'] = json.loads(data_string);
    # end

## departamentos
def getDepartamentos():
    cursor = (database["departamentos"].find({"status": "A"}))
    list_cur = list(cursor)
    data_string = dumps(list_cur)
    data['departamentos'] = json.loads(data_string);
    # end

## departamentos
def getAtendimento():
    cursor = (database["atendimentos"].find({"status": "EA"}))
    list_cur = list(cursor)
    data_string = dumps(list_cur)
    data['atendimentos'] = json.loads(data_string);
    # end

getUsuarios()
getDepartamentos()
getAtendimento()

print(data["atendimentos"])