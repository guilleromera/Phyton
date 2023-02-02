#Sets
#se pueden añadir elementos, no es inmutable
#un set no es una estructura ordenada, no admite repetidos
print("")

my_set=set()
my_otro_set={} #inicialmente es un diccionario

print("La clase es:",type(my_otro_set))
my_otro_set={"Guille","Romera","23"}#añado valores al set
print("La clase es:",type(my_otro_set))
print("La longitud de my_otro_set es:",len(my_otro_set))
print("")

my_otro_set.add("Julio")#se pueden añadir elementos, no es inmutable
print("He añadido 'Julio':",my_otro_set)#un set no es una estructura ordenada, no admite repetidos
print("Esta 'Julio' dentro de my_otro_set?:","Julio" in my_otro_set)
print("Esta 'Julia' dentro de my_otro_set?:","Julia" in my_otro_set)
my_otro_set.remove("Romera")
print("Muestro el set despues de borrar 'Romera':",my_otro_set)
my_otro_set.clear()#borro el set 
print("Imprimo el set que ahora esta vacío:",my_otro_set)
del my_otro_set
# print(my_other_set) NameError: name 'my_other_set' is not defined
print("")

my_set={"Guille","Romera",23}
my_list=list(my_set)
print("Imprimo la lista al completo",my_list)
print("Imprimo el primer elemento:",my_list[0])
my_otro_set={"Kotlin","Swift","Python"}#añado valores al otro set en cuestión
my_new_set=my_set.union(my_otro_set)#concateno los set
print("Imprimo la concatenacion de los set:",my_new_set)
print("No me deja unir set que tienen datos repetidos:",my_new_set.union(my_new_set).union(my_set))#como no se pueden repetir elementos, no hace nada
print("Hago una union a datos nuevos:",my_new_set.union({"Hola","Perra"}))
print("Diferencio con las variables que haya en my_set:",my_new_set.difference(my_set))#no sale la parte de union anterior porque no está guardado en variable
print("Como vemos, la union se puede hacer pero hay que guardarlo a una variable para que sea efectivo")