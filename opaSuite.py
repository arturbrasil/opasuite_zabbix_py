import pymongo
from bson.json_util import dumps
from bson import ObjectId

mydb = pymongo.MongoClient("mongodb://127.0.0.1:27017/")["suite"]

# EXEMPLO
cursor = (mydb["usuarios"].find())
list_cur = list(cursor)
json_data = dumps(list_cur, indent = 3)
print(json_data)

teste = {
  "firstName": "John",
  "lastName" : "doe",
  "age"      : 26,
  "address"  : {
    "streetAddress": "naist street",
    "city"         : "Nara",
    "postalCode"   : "630-0192"
  },
  "phoneNumbers": [
    {
      "type"  : "iPhone",
      "number": "0123-4567-8888"
    },
    {
      "type"  : "home",
      "number": "0123-4567-8910"
    }
  ]
}

data = {}

data["teste"] = {
  "firstName": "John",
  "lastName" : "doe",
  "age"      : 26,
  "address"  : {
    "streetAddress": "naist street",
    "city"         : "Nara",
    "postalCode"   : "630-0192"
  },
  "phoneNumbers": [
    {
      "type"  : "iPhone",
      "number": "0123-4567-8888"
    },
    {
      "type"  : "home",
      "number": "0123-4567-8910"
    }
  ]
}

data["teste2"] = {
  "firstName": "John",
  "lastName" : "doe",
  "age"      : 26,
  "address"  : {
    "streetAddress": "naist street",
    "city"         : "Nara",
    "postalCode"   : "630-0192"
  },
  "phoneNumbers": [
    {
      "type"  : "iPhone",
      "number": "0123-4567-8888"
    },
    {
      "type"  : "home",
      "number": "0123-4567-8910"
    }
  ]
}




print(data)





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