#Funciones
#Las funciones son los conocidos métodos, que nos sirven para realizar tareas --> Java=métodos
print("")

#la palabra reservada para la creacion es 'def'
def mi_funcion():
    print("Esto es una funcion")
mi_funcion() #ejecucion de la funcion/método


def suma_valores(primer_valor,segundo_valor): #con un lenguaje fuertamente tipado podriamos definir el tipo de dato a pedir
    print("La suma de los valores:",primer_valor+segundo_valor)
suma_valores(5,7)
suma_valores(1.3,5.2) #es capaz de hacer la operacion con cualquier tipo siempre que se pueda, aqui con float
suma_valores("5","7") #al no estar fuertemente tipado te concatena 2 strings

def suma_valores_return (primer_valor,segundo_valor):
    return primer_valor+segundo_valor
mi_suma=suma_valores_return(5,10) #tengo que guardar el resultado en una variable
print("La suma de valores con return es:",mi_suma)
print("")

#funcion para imprimir nombre completo con los valores que le pase
def pinta_nombre(nombre,apellido):
    print(f"{nombre} {apellido}")
pinta_nombre("Guille","Romera")
pinta_nombre(apellido="Guille",nombre="Romera") #puedo reordenar el orden que nos impone el print

#funciones con valores por defecto, parecido a DTD
def pinta_nombre_defecto(nombre,apellido,alias="Sin alias"):
    print(f"{nombre} {apellido} {alias}")
pinta_nombre_defecto("Guille","Romera") #coge el tercer valor por defecto definido en el metodo
pinta_nombre_defecto("Guille","Romera","Willy") #le paso ahora el alias

#al meter el asterisco le puedo pasar todos los datos que quiera
def imprime_texto_upper(*texto): #funcion con parametros ordinarios
    for a in texto:
        print(a.upper())
imprime_texto_upper("Hola","Python","Guillermo")


