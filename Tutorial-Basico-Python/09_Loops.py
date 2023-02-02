#Loops
print("")

#While
mi_condicion=0 #creo una varible con valor 0

#si la condicion no cambia en el bucle, sería un bucle infinito
while mi_condicion<10:
    print(mi_condicion)
    mi_condicion +=1 #sumo 1 cada vez que se ejecute el loop
else: #a diferencia de muchos lenguajes los bucles en Python tienen else
    print("Mi condicion es mayor o igual a 10")
print("La ejecucion continúa\n")

#hago otro bucle que empieza desde el nº 10 que se quedo en el anterior bucle
while mi_condicion<20:
    mi_condicion+=1
    if mi_condicion==15: #solo si el numero es 15 ejecuta el print y break
        print("Se detiene la ejecucion en:",mi_condicion)
        break
    print(mi_condicion)
print("")


#For

mi_lista=[35,24,62,52,30,30,17] #defino una lista con 7 valores
print("Recorro una lista con un for:")
for a in mi_lista:
    print (a)

mi_tupla=(35,24,62,52,30,30,17)
print("Recorro una tupla con un for:")
for a in mi_tupla:
    print (a)

#en un set no puede haber elementos repetidos por lo que el 30 solo aparece 1 vez
mi_set = {35,24,62,52,30,30,17}
print("Recorro un set con un for, sin números repetidos:")
for a in mi_set:
    print (a)

mi_dic={"Nombre":"Guillermo","Apellido":"Moure","Edad":23,1:"Python"}
print("Recorro un dict con un for, solo recorre las keys:")
for a in mi_dic:
    print (a)
print("Recorro un dict con un for, solo recorre los values:")
for a in mi_dic.values():
    print(a)
    if a==23:
        break #si se cumple sale del for
else: #solo entra aquí si nunca se cumple el if
    print("El bucle ha finalizado")
print("")

for a in mi_dic.values():
    print(a)
    if a==23:
        continue #vuelve al for sin ejecutar lo que hay debajo
    print("Se ejecuta")
else: #solo entra aquí si nunca se cumple el if
    print("El bucle ha finalizado")
