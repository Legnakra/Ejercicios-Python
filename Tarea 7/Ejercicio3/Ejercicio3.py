#Ejercicio
#Crea un programa python con un diccionario que tenga el contenido del fichero metallica.txt
#Realiza un programa que muestre las siguientes informaciones:
    #El número de discos de Metallica
    #El nombre de todos los discos de Metallica,el número de canciones que tiene cada uno y el número de reproducciones que ha tenido.
    #Pide por teclado el nombre de un disco y muestra el título de las canciones. Si no existe el disco da un error.
    #Pide por teclado una etiqueta y muestra los títulos de los discos que tiene esa etiqueta y las urls donde encontramos las imágenes.
########################################################################


from metalica import metalica
existe=0
print("\n")
print ("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
print("1. Mostrar títulos de todos sus discos.")
print("2. Mostrar las canciones del album solicitado.")
print("3. Buscar disco y muestra sus canciones.")
print("4. Buscar etiqueta.")
print("0. Salir.")
print ("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
opcion = int(input("Elija una opción: "))
num_canciones = 0
while opcion !=0:
#Imprime los discos de Metallica.
    if opcion == 1:
        print("Los discos del grupo son: ",)
        for album in metalica:
            print(album.get("album").get("name") )
#Imprime las canciones del album solicitado
    elif opcion == 2:
        for album in metalica:
            print ("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
            print("Titulo del album: ",album.get("album").get("name"))
            for track in album.get("album").get("tracks").get("track"):
                num_canciones = num_canciones+1
            print ("El album tiene", num_canciones, "canciones.")
            num_canciones = 0
            for track in album.get("album").get("tracks").get("track"):
                reproducciones = track.get("streamable").get("playcount")
                print ("La canción", track.get("name"), "tiene", reproducciones, "reproducciones.")        
#Busca un disco e imprime sus canciones.
    elif opcion ==3:
        album = input("¿Qué album desea buscar?: ")
        for element in metalica:
            if album == element.get("album").get("name"):
                    print ("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
                    print ("El album", album," tiene las siguientes canciones.")
                    print ("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
                    for track in element.get("album").get("tracks").get("track"):
                        print (track.get("name"))
                        existe=1
        if existe == 0:
           print("El album introducido no existe.")
#Busca etiqueta.
    elif opcion ==4:
        tag = input("Introduzca la etiqueta: ")
        for element in metalica:
            for tags in element.get("album").get("tags").get("tag"):
                if tag == tags.get("name"):
                    print ("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
                    print ("El album ",element.get("album").get("name"),"tiene el tag.")
                    print ("Imágenes del album: ")
                    for images in element.get("album").get("image"):
                        print (images.get("#text"))
        else:
            print("La etiqueta introducida no existe.")
    else:    
        print ("Valor no válido. Ingrese la opción correcta.")
    print ("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
    opcion = int(input("Elija una opción: "))
    print ("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
print("Adiós.")