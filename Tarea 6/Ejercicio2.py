#Ejercicio
#Repite el ejercicio 1 con la siguiente estructura de datos: vamos a usar una lista artículos donde vamos a guardar listas con dos elementos: el nombre del artículo y su precio. 
#Ejemplo: articulos=[["fregona",12],["cepillo",14],["recogerdor",23]]
########################################################################


articulos =[]
num_articulos = int(input("¿Cuántos artículos va a introducir?: "))
existe=0
for i in range (num_articulos):
    print("Articulo",i,":")
    nombre = input("Introduzca el nombre del articulo: ")
    precio = int(input("Precio del artículo: "))
    print("- - - - - - - - - - - - - - ")
    articulos.append([nombre,precio])
print("\n")
print ("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
print("1. Precio medio de los artículos.")
print("2. El nombre de los artículos que valen más de 100 euros.")
print("3. Ingresar el nombre de un artículo y mostrar su precio.")
print("0. Salir.")
print ("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
opcion = int(input("Elija una opción: "))
print ("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
while opcion !=0:
    if opcion == 1:
        suma = 0
        for fila in articulos:
            suma=fila[1]+suma
        print ("El precio medio de los articulos es de: ",((suma) / num_articulos))
    elif opcion == 2:
          for elemento in articulos:
            if elemento[1] >= 100:
                print ("El articulo", (elemento[0]), "vale más de 100€, y su precio es de: ", (elemento[1]), "€")  
    elif opcion == 3:
        buscar_articulo = input("¿Qué artículo desea buscar?: ")
        for elemento in articulos:
            if buscar_articulo in elemento:
                print("El artículo", elemento[0], "tiene un precio de", (elemento[1]), "€.")
                existe=1
        if existe == 0:
            print("El articulo", buscar_articulo, "no existe.")
    else:
        print ("Valor no válido. Ingrese la opción correcta.")
    print ("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
    opcion = int(input("Elija una opción: "))
    print ("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
print("Adiós.")