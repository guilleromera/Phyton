print("Sumo 4+2:",4+2)
print("Resto 4-2:",4-2)
print("Multiplico 4*2:",4*2)
print("Divido 4/2:",4/2)
print("Cojo el modulo de la division 10 y 3:",10%3)
print("Nos devuelve el numero entero de la division 10 y 3:",10//3)#un numero entero de la division aunque tenga resto
print("Potencia 4e2:",4**2)

print("Hola"+" Python"+" esto es la caña!!")#concatenacion
print("hola "+str(5)+"\n")#no puedo concatenar tipos diferentes
print("Hola Python\n"*3)# es como recorrer un for en java para imprimir 5 veces,\n salto de linea

my_float=2.5*2
print("Hola"*int(my_float)+"\n")#si no casteo a int no me hace la operacion por ser float

# Operadores Comparativos
print("3 es mayor que 4:",3>4)
print("3 es menor que 4:",3<4)
print("3 es mayor o igual que 4:",3>=4)
print("3 es menor o igual que 4:",3<=4)
print("3 es igual que 4:",3==4)
print("3 es diferente que 4:",3!=4,"\n")

#comparo strings por longitudes
print("Hola" > "Python")
print("Hola" < "Python")
print("Hola" >= "Zola")  # Ordenación alfabética por ASCII
print(len("aaaa") >= len("abaa"))  # Cuenta caracteres
print("Hola" <= "Python")
print("Hola" == "Hola")
print("Hola" != "Python","\n")

#Operadores Logicos
print(3>4 and "Hola" > "Python")#2 false
print(3>4 or "Hola" > "Python")#2 false
print(3<4 and "Hola" < "Python")#2 true
print(3>4 or ("Zolap" > "Python" and 4==4))#si hay un true ya es true
print(not(3>4))#niega el falso por lo que es true


