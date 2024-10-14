#5. Escribe un programa que genere una multiplicación de dos números del 2 al 10 al azar, pregunte por el resultado y
#diga si se ha dado la respuesta correcta  o no es correcta, y en este caso escribir la correcta.

import random #Se importa random para generar los números aleatorios

n1= random.randint (2,10) #Con randint le decimos entre que números va a oscilar el aleatorio.
n2= random.randint (2,10)

respuestaCorrecta= n1*n2 

respuestaUsuario =int(input(f"Cuánto es {n1} x {n2}: "))

if respuestaUsuario == respuestaCorrecta:
    print ("Respuesta correcta!")
else:
    print("Respuesta incorrecta :(")
                      