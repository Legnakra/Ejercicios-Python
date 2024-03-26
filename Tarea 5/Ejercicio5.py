#Ejercicio
#Vamos a crear un programa que tenga el siguiente menú:
    #1. Añadir número a la lista: Me pide un número de la lista y lo añade al final de la lista.
    #2. Añadir número de la lista en una posición: Me pide un número y una posición, y si la posición existe en la lista lo añade a ella (la posición se pide a partir de 1).
    #3. Longitud de la lista: te muestra el número de elementos de la lista.
    #4. Eliminar el último número: Muestra el último número de la lista y lo borra.
    #5. Eliminar un número: Pide una posición, y si la posición existe en la lista lo borra de ella (la posición se pide a partir de 1).
    #6. Contar números: Te pide un número y te dice cuantas apariciones hay en la lista.
    #7. Posiciones de un número: Te pide un número y te dice en que posiciones está (contando desde 1).
    #8. Mostrar números: Muestra los números de la lista
    #9. Salir
#Nota: Utilizar todos los métodos de las listas que sean necesarios.
########################################################################

lista = []
while True:
    print("\n")
    print("1. Añadir número a la lista.")
    print("2. Añadir número de la lista en una posición.")
    print("3. Longitud de la lista.")
    print("4. Eliminar el último número.")
    print("5. Eliminar un número.")
    print("6. Contar números.")
    print("7. Posiciones de un número.")
    print("8. Mostrar números.")
    print("9. Salir.")
    opcion = int(input("Elija una opción: "))
    if opcion == 1:
        num = int(input("Escriba un número: "))
        lista.append(num)
    elif opcion == 2:
        num = int(input("Escriba un número: "))
        posicion = int(input("Diga una posición (esta debe comenzar en 1): "))
        if posicion > len(lista):
            print("La posición es incorrecta.")
        else:
            lista.insert(posicion - 1,num)
    elif opcion == 3:
        print("La longitud de la lista es de %d" % len(lista))
    elif opcion == 4:
        if len(lista)>0:
            print("El último elemento es %d y lo eliminamos." % lista.pop())
        else:
            print("La lista está vacía.")
    elif opcion == 5:
        posicion = int(input("Diga una posición (esta debe comenzar en 1): "))
        if posicion > len(lista):
            print("La posición es incorrecta.")
        else:
            print("El elemento es %d y lo eliminamos." % lista.pop(posicion - 1))
    elif opcion == 6:
        num = int(input("Escriba un número:"))
        print("El número %d aparece %d veces en la lista." % (num,lista.count(lista)))
    elif opcion == 7:
        num = int(input("Escriba un número:"))
        in_buscar = 0
        print("Las posiciones del numero: ",end="")
        for indice in range(0,lista.count(num)):
            ind_buscar = lista.index(num,in_buscar)
            ind_buscar +=1
            print(in_buscar," ",end="")
        print()
    elif opcion == 8:
        for num in lista:
            print(num," ",end="")
        print()
    elif opcion == 9:
        break
    else:
        print("La opción es incorrecta.")