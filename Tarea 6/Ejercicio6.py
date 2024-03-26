#Ejercicio
#Utilizando el ejercicio anterior, crea una aplicación simple de craqueo de contraseñas utilizando los ficheros que puedes encontrar en el repositorio.
########################################################################
#usuario = maria
#contraseña =maria
########################################################################

from mmap import MAP_PRIVATE
from threading import main_thread
from crypt import crypt
import readline
usuario = (input("Usuario: "))
f = open("password.txt")
lineas = f.readlines()
f.close()
g = open ("diccionario.txt")
diccionario = g.read().splitlines()
g.close()
encontrado = False
for u in lineas:
    lista = u.split(":")
    if usuario == lista[0]:
        print("El usuario existe.") 
        encontrado = True
        for contraseña in diccionario:
            sal = lista[1][0:30]
            encriptado = crypt(contraseña,sal)
            valido = False
            if encriptado == lista[1]:
                print("Una de las contraseñas del diccionario es correcta. La contraseña del usuario" ,usuario ,"es" ,contraseña)
                valido = True
        if not valido:
                print("La contraseña no está en el diccionario.")
if not encontrado:
        print("El usuario no existe.")