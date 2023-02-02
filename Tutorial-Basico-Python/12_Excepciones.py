##Excepciones
print("")

numUno=1
numDos=5
numDos="5"

#trato las excepciones con try/except
try:
    print(numUno+numDos)
    print("No se ha producido un error")
except:
    print("Se ha producido un error") #se mete aqui porque estoy intentando sumar un int y un str

#try except else,else solo se ejecuta si no lo hace la excepción
try:
    print(numUno+numDos)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else:
    print("La ejecucion continua correctamente") #este else solo se ejecuta si no se ejecuta la except
finally:
    print("La ejecucion continúa") #esto se ejecuta siempre, pase lo que pase

#Excepciones por tipo
try:
    print(numUno+numDos)
    print("No se ha producido un error")
except TypeError: #solo captura errores de tipo TypeError
    print("Se ha producido un TypeError")
except ValueError: #solo captura errores de tipo ValueError
    print("Se ha producido un ValueError")


#Captura de la informacion de la excepcion
try:
    print(numUno+numDos)
    print("No se ha producido un error")
except TypeError as error: #capturo la informacion de la excepción
    print(error)
except ValueError as error: #capturo la informacion de la excepcion ValueErrors
    print(error)
