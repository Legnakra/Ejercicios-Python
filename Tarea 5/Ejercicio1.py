#Ejercicio
#Pedir cadenas de caracteres y guardarlas en una lista (el programa pedirá al principio cuantas cadenas se van a introducir). 
#A continuación se pide otra cadena, y hay que eliminar de la lista todas las apariciones de esta segunda cadena. 
#Si se ha quitado algún elemento se muestra la lista, sino se informa que la segunda cadena no estaba en la lista.
########################################################################

lista= []
num_cadenas = int(input("¿Cuántas cadenas se van a introducir?: "))
for i in range (num_cadenas):
    cadena = input("Escriba una cadena de caracteres: ")
    lista.append(cadena)
otra_cadena = input("Introduzca otra cadena: ")
if otra_cadena in lista:
    lista.remove(otra_cadena)
    print (lista)
else:
    print("La segunda cadena no se encuentra en la lista de cadenas.")