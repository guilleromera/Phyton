##Modulos
print("")

import mi_modulo #importo el modulo al completo y tengo que llamar a sus funciones

mi_modulo.sum_numeros(1,2,3)
mi_modulo.printValue("Hola Python")

from mi_modulo import sum_numeros,printValue #importo unicamente las funciones concretas del modulo

sum_numeros(1,2,3)
printValue("Hola Chiquis")
print("")

import math #importo el modulo math 

print(math.pi) #llamo a la funcion o metodo pi
print(math.pow(2,5))

from math import pi as pi_value #importo la funcion pi del modulo math como 'pi_value'

print(pi_value)