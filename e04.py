#4. Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable,
#y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.

peso= float(input("Introduzca su peso en kilogramos: "))
estatura= float(input("Introduzca su estatura en metros: "))

imc= peso/(estatura**2) #peso dividido por estatura elevado a 2


imcRedondeado= round (imc,2)#Para redondear imc a 2 decimales.

print (f"Tu índice de masa corporal es {imc}")



