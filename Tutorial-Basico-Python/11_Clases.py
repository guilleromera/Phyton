## Clases
print("")

#los nombres de las clases funcionan con camel case
class PersonaVacia:
    pass

#Ejemplo constructor por partes
class Persona:
    def __init__(self, nombre, apellido): #me crea el metodo constructor de clase
        self.nombre=nombre #hace referencia al propio objeto, this en java
        self.apellido=apellido
mi_persona= Persona("Guillermo","Romera")
print(f"{mi_persona.nombre} {mi_persona.apellido}") #tengo que llamar a cada uno de sus atributos
print("")


#Ejemplo constructor completo clase Person
class Person:
    def __init__(self, nombre, apellido,alias="Sin alias"): #me crea el metodo constructor de clase
        self.nombreCompleto=f"{nombre} {apellido} ({alias})" #unifico todos los valores, son públicos
        self.__nombre=nombre #variables privadas, solo de lectura, no escritura
    
     #método para devolver las variables privadad, Getters en java
    def get_nombre(self):
        return self.__nombre

    def caminar (self): #añado el método o función caminar y llamo a this o self en Python
        print(f"{self.nombreCompleto} está caminando")

mi_person= Person("Guillermo","Romera")
print(mi_person.nombreCompleto)
mi_person.caminar()

mi_otra_persona= Person("Guillermo","Romera","Gea") #defino ahora un alias en el costructor
print(mi_otra_persona.nombreCompleto)
print("Accedo solo al nombre privado:",mi_otra_persona.get_nombre()) #Getter de java, solo de lectura
mi_otra_persona.caminar()

mi_otra_persona.nombreCompleto="Allen Iverson (The answers)" #cambio los valores para mi_otra_persona
print(mi_otra_persona.nombreCompleto)
mi_otra_persona.caminar()
print("")