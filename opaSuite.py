import pymongo
from bson.json_util import dumps
from bson import ObjectId

dados = {}

mydb = pymongo.MongoClient("mongodb://127.0.0.1:27017/")["suite"]

##############
cursor = (mydb["departamentos"].find({"status": "A"}))
list_cur = list(cursor)
json_data = dumps(list_cur)
##############

dados['departamento'] = json_data

print(list_cur['empresa'])

""" usuarios = (mydb["usuarios"].find({"status": "A"}))
list_cur = list(usuarios)
json_data = dumps(list_cur)
print(json_data)
##############
temp_dict = {}
temp_dict['usuarios'] = json_data
data.append(temp_dict)

# get mongo data 3
em_atendimento = (mydb["atendimentos"].find({"status": "EA"}))
list_cur = list(em_atendimento)
json_data = dumps(list_cur)
print(json_data)
##############
temp_dict = {}
temp_dict['em_atendimento'] = json_data
data.append(temp_dict) """







""" if item == "getAllUsuarios":
    cursor = (mydb["usuarios"].find())
    list_cur = list(cursor)
    json_data = dumps(list_cur)
    print(json_data)

if item == "getDepartamentos":
    departamentos = (mydb["departamentos"].find({"status": "A"}))
    list_cur = list(departamentos)
    json_data = dumps(list_cur)
    print(json_data)

if item == "getFinalizados":
    finalizados = (mydb["atendimentos"].find({"status": "F"}))
    list_cur = list(finalizados)
    json_data = dumps(list_cur)
    print(json_data)

if item == "getEmAtendimento":
    emAtendimento = (mydb["atendimentos"].find({"status": "EA"}))
    list_cur = list(emAtendimento)
    json_data = dumps(list_cur)
    print(json_data)

if item == "getAguardandoAtendimento":
    var = (mydb["atendimentos"].find({"status": "AG"}))
    list_cur = list(var)
    json_data = dumps(list_cur)
    print(json_data)

if item == "getEmEAguardandoAtendimento":
    var = (mydb["atendimentos"].find({"status": "AG"}))
    list_cur = list(var)
    json_data = dumps(list_cur)
    print(json_data)

if item == "atendente":
    print(mydb["atendimentos"].count_documents({"status":"EA","id_atendente": ObjectId(params[2])}))

if item == "AGsetor":
    print(mydb["atendimentos"].count_documents({"status": "AG","setor": ObjectId(params[2])}))

if item == "setor":
    print(mydb["atendimentos"].count_documents({"status": params[2],"setor": ObjectId(params[3])}))

if item == "finalizadoHoje":
    print(mydb.atendimentos.count_documents({"status":"F","id_atendente":ObjectId(params[2])})) """