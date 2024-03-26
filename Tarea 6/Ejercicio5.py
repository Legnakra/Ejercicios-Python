#Ejercicio5
#Implementa un sistema completo de validación de usuarios en una máquina con Debian, que tiene las siguientes características:
#El nombre de usuario y las contraseñas se almacenan en el fichero /etc/shadow, al que tiene acceso sólo el usuario root.
#Las contraseñas se almacenan como un hash AES512 con sal
#Ayuda:
    #Supongamos que tenemos en nuestro sistema el usuario prueba con contraseña asdasd, una línea correspondiente a este usuario en el fichero /etc/shadow sería:
    #La sal de una contraseña cifrada (en debian 11) se indica en linux por los 30 primeros caracteres del hash de la contraseña, en el caso anterior la sal sería $y$j9T$bU9gdaTeFdFmE.H6YFABA/$.
    #La función crypt del módulo crypt permite formar los hashes con sal utilizados por linux, de la siguiente manera:
        #donde asdasd es la contraseña en claro.

#Escribe un programa que lea un usuario y una contraseña, y te informe si el usuario es válido o no.
########################################################################

f = open ("passwd.txt")
lineas = f.readlines()
f.close
print (lineas)
lista = []
for linea in lineas:
    lista.append(linea.split(":"))
nombre = input ("Introduzca el nombre del usuario: ")
encontrado =False
for usuario in lista:
    if nombre == usuario [0]:
        encontrado=True
        sal = usuario[1][:30]
        contraseña = input("La contraseña es: ")
if not encontrado:
        print ("El usuario no existe.")