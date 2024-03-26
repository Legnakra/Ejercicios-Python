#Ejercicio
#Realiza un programa que pida un cadena. A continuación debe pedir otra cadena. El programa debe buscar la segunda cadena en la primera (ignorando mayúsculas o minúsculas) y podrá responder una de las siguientes opciones:
#La segunda cadena es una subcadena de la primera
#La segunda cadena no es una subcadena de la primera
########################################################################
#Análisis:
    #Problema:
    #Entrada:
    #Salida:
########################################################################
#Diseño:
    #1.
    #2.
    #3.
########################################################################

cadena = input("Escriba una cadena de caracteres: ")
subcadena = input("Escriba una subcadena de caracteres: ")
while subcadena in cadena:
    print("Respuesta: ")
    print("La segunda cadena es una subcadena de la primera.")
    break
else:
    print("La segunda cadena NO es una subcadena de la primera.")