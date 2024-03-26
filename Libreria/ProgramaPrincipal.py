from Libreriajson import *
leer_ficheros = leer_json("libreria.json")

#Ejercicio 1
print ("Hay un total de ",contar_libros(libreria),"libros.")

#Ejercicio 2
minimo= float(input("Precio mínimo: "))
maximo= float(input("Precio maximo: "))
libros= seleccionar_por_precio(libreria,preciomin, preciomax)
for libro in libros:
    print (libro)

#Ejercicio 3
titulo =input("Escribe el título de un libro: ")
lista = seleccionar_por_titulo(libreria, titulo)
for titulo, año in lista:
        print (titulo, año)

#Ejercicio 4
libros, autores = ver_titulos_autores(libreria)
for titulo, autor in zip (libros, autores):
    print (titulo)
    for a in autor:
        print (a)