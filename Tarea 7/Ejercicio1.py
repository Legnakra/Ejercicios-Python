#Copia este diccionario en un fichero python, que representa los datos de una película:
from pelicula import pelicula

print("\n")
print ("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
print("1. Mostrar título y año de la película.")
print("2. Mostrar elenco.")
print("3. Mostrar puntuación media de la película.")
print("0. Salir.")
print ("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
opcion = int(input("Elija una opción: "))
while opcion !=0:
	if opcion ==1:
		print ("El título de la película es", pelicula.get("title"), " del año", pelicula.get ("year"))
		print ("Su argumento es ", pelicula.get ("storyline"))
	elif opcion ==2:
		print("El elenco que conforma la película", pelicula.get("title"),"es: ", pelicula.get("actors"))
	elif opcion ==3:
		print ("La puntuación media de la película es: ", sum(pelicula.get("ratings"))/ len(pelicula.get("ratings")))
	else:    
		print ("Valor no válido. Ingrese la opción correcta.")
	print ("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
	opcion = int(input("Elija una opción: "))
	print ("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
print("Adiós.")
