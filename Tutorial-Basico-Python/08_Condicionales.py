##Condicionales
##las condiciones necesitan tabulaciones
print("")
mi_condicion= True

if mi_condicion: #es lo mismo que if my_condicion=True:
    print("Se ejecuta la condicion del if")


mi_condicion=5*5
if mi_condicion !=11:
    print("Se ejecuta la condicion del segundo if")

if mi_condicion >10 and mi_condicion<20:
    print("Es mayor que 10 y menor que 20")
elif mi_condicion==25:
    print("Es igual a 25")
else:
    print("Es menor o igual que 10 o mayor o igual que 20 o distinto de 25")
print("La ejecucion continúa\n")


mi_string=""
if mi_string: #si no está vacia devuelve el primer print
    print("Mi cadena de texto no es vacía")
else:
     print("Mi cadena de texto es vacía y su longitud es:",len(mi_string))
if not mi_string: #comprueba si está vacio la cadena de texto
    print("Mi cadena de texto esta vacia")

