#Strings 

#concatenacion de Strings
var_string="Mi String"
var_other_string="Mi String"

print(var_string+" "+var_other_string)
print("")

#Variable multilinea
multiline_string = '''I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python.''' #igual que un comentario puedo hacer un string en varias lineas, tambien valen " "
print(multiline_string)
print("")

#Formateo
nombre, apellidos, edad="Guillermo","Romera Moratalla", 23
nombre_entero=nombre+" "+apellidos+" "+str(edad)
#print(nombre_entero)
print("Mi nombre es "+nombre+" "+apellidos+" y mi edad es "+str(edad))#hay que castear el int a str
#las 2 siguientes lineas son exactamente lo mismo
print(f"Mi nombre es {nombre} {apellidos} y mi edad es {edad}")#es lo mismo que la de abajo, es la manera más correcta
print("Mi nombre es {} {} y mi edad es {}".format(nombre,apellidos,edad))#es lo mismo que la de arriba
print("Mi nombre es %s %s y mi edad es %d" %(nombre,apellidos,edad))
print("")

# Desempaqueado de caracteres
language = "python"
a, b, c, d, e, f = language
print(a)
print(e)
print("")

# División

#imprimedel caracter 1 incluido hasta el 3 sin incluir 
language_slice = language[1:3]
print(language_slice)

#imprime del cracter 1 al final
language_slice = language[1:]
print(language_slice)

#caracter -2 empezando por el final es una o
language_slice = language[-2]
print(language_slice)

#del 0 al 6 en un rango de 2 en 2
language_slice = language[0:6:2]
print(language_slice)
print("")

# Imprime al revés
reversed_language = language[::-1]
print(reversed_language)
print("")

# Funciones del lenguaje
print(language.capitalize())#imprime la primera letra en mayuscula
print(language.upper())#todas en mayuscula
print(language.count("t"))#cuenta las t
print(language.isnumeric())#es numerico?
print("1".isnumeric())#es numerico?
print(language.lower())#convierte a minusculas todo
print(language.lower().isupper())#convierto todo a minusculas y pregunto si esta en mayusculas
print(language.startswith("py"))#pregunto si empieza con py
print("Py" == "py")# No es lo mismo