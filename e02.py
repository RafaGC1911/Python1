#2. Escribe un programa que pregunte el nombre y después de que el usuario lo introduzca muestre por pantalla el nombre en mayúsculas
#y el número de caracteres que tiene. Después deberá escribir el nombre tantas veces como letras contiene el nombre en líneas distintas.

nombre= input("Cual es tu nombre?: ")

nombreMayusculas= nombre.upper()
numCaracteres= len(nombre)

print (f"Nombre en mayúsculas: {nombreMayusculas}")
print (f"Tu nombre tiene: {numCaracteres}  caracteres")

for i in range (numCaracteres):
    print (nombre)