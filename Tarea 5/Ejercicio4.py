#Ejercicio
#Escriba un programa que permita crear una lista de palabras y que, a continuación dé tres opciones:
    #Contar: Me pide una cadena, y me dice cuantas veces aparece en la lista.
    #Modificar: Me pide una cadena, y otra cadena a modificar, y modifica todas las apariciones de la primera por la segunda en la lista.
    #Eliminar: Me pide una cadena, y la elimina de la lista.
#El programa te muestra el menú, hasta que introduzcamos la opción 0 de salir.
########################################################################

lista= []
num_palabras = int(input("¿Cuántas palabras tiene la lista?: "))
for i in range (num_palabras):
    cadena = str(input("Escriba la palabra: "))
    lista.append(cadena)
print("La lista creada es:" ,lista)
print("\n")
print("1. Contar")
print("2. Modificar")
print("3. Eliminar")
print("0. Salir")
opcion = int(input("Escriba su opción:"))
while opcion !=0:
    if opcion ==1:
        contar = input("Dígame la palabra a buscar: ")
        if lista.count(contar) == 0:
            print("La palabra ",contar," no aparece.")
        elif lista.count(contar) == 1:
            print("La palabra ",contar,"aparece 1 vez.")
        elif lista.count(contar) > 1:
            print("La palabra",contar, "aparece",lista.count(contar),"veces.")
    elif opcion == 2:
        cadena = input("Sustituir la palabra: ")
        subcadena = input("por la palabra: ")
        print("La lista es ahora: ")
        indice = 0
        for elemento in lista:
            if elemento == cadena:
                lista[indice] = subcadena
            indice += 1
        for elemento in lista:
            print(elemento," ",end="")
    elif opcion == 3:
        eliminar = input("La palabra a eliminar es: ")
        if eliminar in lista:
            while eliminar in lista:
                lista.remove(eliminar)
            print("La lista es ahora: ",lista)
        else:
            print("La cadena introducida no se encuentra en la lista.")
    print("\n")
    print("1. Contar")
    print("2. Modificar")
    print("3. Eliminar")
    print("0. Salir")
    opcion = int(input("Escriba su opción:"))
print("¡Adiós!")