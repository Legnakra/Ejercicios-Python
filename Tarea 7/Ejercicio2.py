#Muestra el nombre y el argumento de cada película.
#Muestra el nombre y los actores de cada pelicula.
#Pide por teclado un genero y muestra el nombre de las péliculas de ese género.
#Pide un año por teclado y muestra todas las péliculas anteriores a ese año.
###########################################################################################
from peliculas import peliculas

print("\n")
print ("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
print("1. Mostrar nombre de la película y argumento de las películas.")
print("2. Mostrar nombre de la película y su elenco.")
print("3. Mostrar género y películas del mismo.")
print("4. Mostrar películas anteriores a el año indicado.")
print("0. Salir.")
print ("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
opcion = int(input("Elija una opción: "))
print ("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
while opcion !=0:
	if opcion ==1:
		for peliculas in peliculas:
			print ("El título de la película es", peliculas.get("title"))
			print ("Su argumento es ", peliculas.get("storyline"))
			print ("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
	elif opcion ==2:
		for peliculas in peliculas:
			print ("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
			print("El elenco que conforma la película", peliculas.get("title"),"es: ", peliculas.get("actors"))
	elif opcion ==3:
		genero = float("Introduzca el género: ")
		for generos in peliculas.get("genres"):
			if genero == peliculas.get("genres"):
				print ("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
				print ("La pelicula ",peliculas.get("title"),"pertenece al género.")
	elif opcion==4:
		año = int(input("Introduzca un año: "))
		for year in peliculas:
			if peliculas.get("year") <= año:
				print( "Las películas anteriores a ese año son: ", peliculas.get("title"))
	else:    
		print ("Valor no válido. Ingrese la opción correcta.")
	print ("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
	opcion = int(input("Elija una opción: "))
	print ("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
print("Adiós.")