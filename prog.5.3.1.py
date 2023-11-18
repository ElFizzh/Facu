import json
# se crea un objeto de muestra, para serializar,
Original=[
 ['correo','nombre','telefono'],
 ['juan@gmail.com','Juan','8123232323'],
 ['maria@gmail.com','Maria','5545454545'],
 ['diana@homail.com','Diana','4490909090']
]

print (">>Tipo del objeto.\n")
print(type(Original))
print("\n>> Contenido del objeto. \n ")
print(Original)
print("\n>> Serializacion a JSON. \n ")
Original_JSON=json.dumps(Original,indent=4)
print(Original_JSON)
print("\n>> Deserializacion desde JSON. \n ")
Nueva_Lista=json.loads(Original_JSON)
print(Nueva_Lista)
print(type(Nueva_Lista))
print("\n>>Comprobando iagualdad de objetos. \n ")
print(Original==Nueva_Lista)