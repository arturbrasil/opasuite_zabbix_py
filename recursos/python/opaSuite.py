import sys
import pymongo
from bson.json_util import dumps
# from bson import ObjectId

params = sys.argv
item = params[1]
mydb = pymongo.MongoClient("mongodb://127.0.0.1:27017/")["suite"]

if item == "getUsuariosAtivos":
    usuarios = (mydb["usuarios"].find({"status": "A"},{'nome','online'}))
    list_cur = list(usuarios)
    json_data = dumps(list_cur)
    print(json_data)

if item == "getCanais":
    canais = (mydb["canal_comunicacaos"].find({"status": "A"}))
    list_cur = list(canais)
    json_data = dumps(list_cur)
    print(json_data)

if item == "getDepartamentos":
    departamentos = (mydb["departamentos"].find({"status": "A"},{'status','nome'}))
    list_cur = list(departamentos)
    json_data = dumps(list_cur)
    print(json_data)

if item == "getEmAtendimento":
    emAtendimento = (mydb["atendimentos"].find({"status": "EA"},{'status','setor','id_atendente','canal_id','canal'}))
    list_cur = list(emAtendimento)
    json_data = dumps(list_cur)
    print(json_data)

if item == "getAguardando":
    atendimentos = (mydb["atendimentos"].find({"status": "AG"},{'status','setor','id_atendente','canal_id','canal'}))
    list_cur = list(atendimentos)
    json_data = dumps(list_cur)
    print(json_data)

if item == "getAtendimentos":
    atendimentos = (mydb['atendimentos'].find({'$or':[{'status':'AG'},{'status':'EA'}]},{'status','setor','id_atendente','canal_id','canal'}))
    list_cur = list(atendimentos)
    json_data = dumps(list_cur)
    print(json_data)
