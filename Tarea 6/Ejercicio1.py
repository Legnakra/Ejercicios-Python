#Ejercicio
#Queremos guardar el nombre de los artículos de un almacén y sus precios. Como estructura de datos vamos a usar dos listas:
    #artículos, donde vamos a guardar el nombre de los artículos
    #precios donde vamos a guardar los precios.
#De tal forma que el artículo en la posición n de la lista artículos tendrá el precio correspondiente a la misma posición en la lista precios.
#Realiza un programa que pida por teclado artículos y sus precios (el programa pedirá cuantos artículos se van a introducir), al finalizar dará la siguiente información:
    #El precio medio de los artículos.
    #El nombre de los artículos que valen más de 100 euros.
    #Nos pedirá un nombre de un artículo y si existe nos dará su precio, sino nos dará un error.
########################################################################

lista_articulos = []
lista_precio = []
num_articulos = int(input("¿Cuántos artículos va a introducir?: "))
for i in range (num_articulos):
    articulos = input("Escriba el nombre del artículo: ")
    precio = float(input("Precio del artículo: "))
    lista_articulos.append(articulos)
    lista_precio.append(precio)
print("\n")
print ("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
print("1. Precio medio de los artículos.")
print("2. El nombre de los artículos que valen más de 100 euros.")
print("3. Ingresar el nombre de un artículo y mostrar su precio.")
print("0. Salir.")
print ("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
opcion = int(input("Elija una opción: "))
while opcion !=0:
    if opcion == 1:
        print ("El precio medio de los articulos es de: ",((sum(lista_precio)) / num_articulos))
    elif opcion == 2:
        for precio in lista_precio:
            if precio >= 100:
                posicion = lista_precio.index(precio)
                print ("El articulo", (lista_articulos[posicion]), "vale mas de 100€, y su precio es de: ", (lista_precio[posicion]), "€")
    elif opcion == 3:
        buscar_articulo = input("¿Qué artículo desea buscar?: ")
        if buscar_articulo in lista_articulos:
            posicion = lista_articulos.index(buscar_articulo)
            print ("El artículo", buscar_articulo, "tiene un precio de %d €." %(lista_precio[posicion]))
        else:
            print("El articulo con dicho nombre no existe.")
    elif opcion:
        print ("Valor no válido. Ingrese la opción correcta.")
    print ("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
    opcion = int(input("Elija una opción: "))
    print ("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
print("Adiós.")