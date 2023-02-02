#Listas

my_lista=list()
my_otra_lista=[]#asi se puede definir una lista

print("")
print("La longitud de la lista es:",len(my_lista))
#relleno la lista
my_lista=[35,24,2,45,62,8,17]
print("Imprimo my_lista:",my_lista)
print("La longitud de la lista es:",len(my_lista))

my_otra_lista=[35,1.77,"Guille","Romera"]
print("")

#Acceso a elementos y búsqueda
print("Imprimo el primer valor:",my_otra_lista[0])
print("Imprimo el segundo valor:",my_otra_lista[1])
print("Imprimo el ultimo valor:",my_otra_lista[-1])
print("Imprimo el penultimo valor:",my_otra_lista[-2])
print("Devuelve el valor -4 empezando por el ultimo (empieza en indice -1):",my_otra_lista[-4])
print("¿Cuantos valores 35 hay en my_otra_lista?",my_otra_lista.count(35))#Retorna el numero de ocurrencias del valor

#asigna cada una de estas variables a sus valores respectivos en la lista, tiene qe haber las mismas variables que valores en la lista
edad,altura,nombre,apellido=my_otra_lista
print("Imprimo la edad asociada a my_otra_lista[0]",edad)

name, height, age, surname = my_otra_lista[2], my_otra_lista[1], my_otra_lista[0], my_otra_lista[3]#asigno valores a las variables en funcion de la poscicion de la lista
print("Imprimo el nombre asociada a my_otra_lista[2]",name)
print("")

#Concatenacion de listas
print("Conctanecion de listas en el orden metido:",my_lista+my_otra_lista)
print("")


#Inserto y borro datos en my_otra_lista
print("Inserto valores nuevos en my_otra_lista")
print("my_otra_lista:",my_otra_lista)

my_otra_lista.append("Hola")#inserta el dato en la ultima posicion
print("Inserto hola:",my_otra_lista)

my_otra_lista.insert(1,"Ey")#inserto en la posicion 1
print("Inserto 'Ey en la primera poscion':",my_otra_lista)

my_nueva_lista=my_otra_lista.copy()#creo una nueva lista en este punto que hace emncion a my_otra_lista en ese punto

my_otra_lista[1]="Hola" #Renombro el elemento de la posicion 1,tipado dinamico
print(my_otra_lista)

my_otra_lista.remove("Hola")#Borro el primer elemento que aparezca según lo pedido
print(my_otra_lista)

my_otra_lista.pop()#elimino la utlima posicion de la lista
my_otra_lista.pop(2)#elimina el valor en la posicion 2
print(my_otra_lista)
print("")

my_otra_lista.clear()#elimina la lista entera
print("Muestro la lista borrada completamente:",my_otra_lista)
print("Imprimo my_nueva_lista:",my_nueva_lista)

my_nueva_lista.reverse()#le da la vuelta a la lista
print("Imprimo my_nueva_lista al reves:",my_nueva_lista)

#my_nueva_lista.sort()#Ordeno la lista solo si son del mismo tipo, si no no funciona
#print(my_nueva_lista)

# Cambio de tipo, tipado dinámico, my_lista era de tipo List()
my_lista = "Hola Python"
print(my_lista)
print(type(my_lista))