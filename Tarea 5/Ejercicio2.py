#Ejercicio
#Crear una lista con 10 número aleatorios (del 1 al 100). A continuación se muestra la lista. El programa seguirá mostrando el siguiente menú:
    #1. Sumar
    #2. Máximo
    #3. Media
    #4. Salir
    #Opción:
#Al elegir una opción se realiza la operación:
    #Sumar: Muestra la suma de los números
    #Máximo: Muestra el máximo de la lista
    #Media: Muestra la Media
#El menú se va repitiendo hasta que elegimos la opción 4 (Salir).
########################################################################

from random import randint
lista = []
contador = 0
menu = 0
opcion = 0
num= randint(1,100) 
while contador < 10:
    num = randint(1,100)
    contador+=1 
    lista.append(num)
print ("Esta es la lista de números generada de forma aleatoria." ,lista)
while opcion !=4:
    opcion = int(input("¿Qué operación desea realizar con los numeros de la siguiente lista (1 es suma; 2 muestra el mayor; 3 muestra la media; 4 es para salir)?: "))
    if opcion == 1:
        print ("El resultado de la suma es",sum(lista))
    elif opcion == 2:
        print ("El mayor de toda la consecución es", max(lista))
    elif opcion == 3:
        print ("La media aritmética de la lista es: ", (sum(lista)/10))
    elif opcion !=4:
        print ("Opción incorrecta.")
if opcion == 4:
    print ("Programa cerrado.")