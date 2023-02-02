#Tuplas
print("")

my_tupla=tuple()
my_otra_tupla=()#asi se puede definir una tupla

my_tupla=(23,1.75,"Guillermo","Romera")
my_otra_tupla=(60,30,20)
print("Imprimo la tupla",my_tupla,"y su tipo:",type(my_tupla))
print("Imprimo el valor de la posicion 1:", my_tupla[0])
print("Imprimo el utimo valor de la tupla:", my_tupla[-1])
print("Cuenta los valores que se llaman 'Guillermo':",my_tupla.count("Guillermo"))
print("Nos devuelve la posicion del valor 'Guillermo';",my_tupla.index("Guillermo"))
print("")

my_suma_tuplas=my_tupla+my_otra_tupla #concatenación de tuplas
print("Concatenacion de tuplas:",my_suma_tuplas)
print("Saco los valores de la tupla del 3 incluido al 6 sin incluir:",my_suma_tuplas[3:6])
print("")

my_tupla=list(my_tupla) #Convierto la tupla en lista
print("Convierto la tupla a lista",type(my_tupla))

#modificar e insertar valores solo se puede hacer en las listas
my_tupla[0]=24
my_tupla.insert(1,"Rojo")
my_tupla=tuple(my_tupla) #convierto la lista en tupla
print("Reasigno la lista a tupla y muestro valores cambiados y añadidos:",my_tupla,"y su tipo:",type(my_tupla))

#al hacer delete se carga la variable o elemento --> del my_otra_tupla
# name 'my_otra_tupla' is not defined --> print(my_otra_tupla)

#my_tupla[1]=1.77 no puedo alterarla tupla como en la lista, es inmutable
#my_tupla[5]=1.8 tampoco puedo hacer esto, es inmutable  object does not support item assignment
