"""
print("")
age=input("¿Cual es tu edad?")
print("La edad introducida es: ",age)
"""

#tiene camel case pero no se suele utilizar
my_variable="Mi variable string";
print(my_variable,";su longitud es:",len(my_variable))

#variable de tipo entero
my_variable_int=5
print(my_variable_int)

#convierto un int a str
variable_int_to_str=str(my_variable_int)
print(variable_int_to_str,";su longitud es:",len(variable_int_to_str))

#concatenacion
print(my_variable,my_variable_int,variable_int_to_str)
print("")


# ¿Forzamos el tipo?
address: str = "Mi dirección"
address = True
#address = 5
#address = 1.2
print(type(address))
print("")

#Variables en una sola linea
name, surname, alias, age = "Guillermo", "Romera", 'Gea', 23
print("Me llamo",name,"mi apellido es",surname,"y mi edad es",age)
print("")

# Inputs para pedir informacion por pantalla, Scanner de java
name = input('¿Cuál es tu nombre? ')
age = input('¿Cuántos años tienes? ')
print(name)
print(age)
print("")

# El tipado de Python es dinámico
address: str = "Mi dirección"
address = True
address = 5
address = 1.2
print("Imprimo el tipo de adress: ",type(address))

