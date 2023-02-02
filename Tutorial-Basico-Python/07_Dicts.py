#Dicts
#Funciona como HashMap en java
print("")

my_dict=dict()
my_otro_dict={}

print("Imprimo el tipo de my_dict:",type(my_dict))
print("Imprimo el tipo de my_otro_dict:",type(my_otro_dict))

my_otro_dict={"Nombre":"Guillermo","Apellido":"Moure","Edad":23,1:"Python"}#añado claves-valor a my_otro_dict
my_dict={
    "Nombre":"Guillermo",
    "Apellido":"Moure",
    "Edad":23,
    "Lenguajes":{"Java","Python","JavaScript"},
    1:1.75
}
print("Imprimo my_otro_dict:",my_otro_dict,"y su longitud es:",len(my_dict))#cuenta 1 len por cada clave-valor
print("Imprimo my_dict:",my_dict,"y su longitud es:",len(my_dict))
print("")

print("Imprimo el valor de 'Nombre' llamando a su clave:",my_dict["Nombre"])#accedo a un valor llamando a una clave
my_dict["Nombre"]="Pedro" #modifico el valor para la clave "Nombre"
print("Imprimo el valor modificado:",my_dict["Nombre"])
my_dict["Calle"]="Calle Diamante" #añado esta clave-valor
print("Imprimo my_dict habiendo añadido datos:",my_dict)
del my_dict["Calle"]
print("Borrando 'Calle' de my_dict:",my_dict)
print("")

print("Busco por clave:","Nombre" in my_dict)#Hay que buscar por clave, no por valor
print("Busco por valor","Guillermo" in my_dict)
print("Retorna los items:",my_dict.items())
print("Retorna las claves",my_dict.keys())
print("Retorna los valores:",my_dict.values())
print("")

""" muy útil para inicializar un nuevo diccionario
con información temporal, como valores iniciales o
mensajes para añadir o actualizar datos. Si no provees el segundo parámetro,
el objeto que arroja es un nuevo diccionario con valores sin asignar"""
my_list = ["Nombre", 1, "Piso"]
my_new_dict = dict.fromkeys((my_list))
print("Devuelve solo las claves del dic: ",my_new_dict)
my_new_dict = dict.fromkeys(("Nombre", 1))
print((my_new_dict))
my_new_dict = dict.fromkeys(my_dict)
print((my_new_dict))
my_new_dict = dict.fromkeys(my_dict, "Guille")
print("Añade el valor 'Guille'a todos las claves",my_new_dict)


