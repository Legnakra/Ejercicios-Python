#Ejercicio
#Crea una aplicación que permita adivinar un número. La aplicación genera un número aleatorio del 1 al 100. A continuación va pidiendo números y va respondiendo si el número a adivinar 
#es mayor o menor que el introducido,a demás de los intentos que te quedan (tienes 10 intentos para acertarlo). El programa termina cuando se acierta el número 
#(además te dice en cuantos intentos lo has acertado), si se llega al limite de intentos te muestra el número que había generado.
########################################################################
#Análisis:
    #Problema:Adivinar un número aleatorio entre 1 y 100.
    #Entrada:
    #Salida:
########################################################################
#Diseño:
    #1.Generar un número aleatorio entre 1 y 100.
    #2.Mostrar 10 intentos.
    #3.Leer num.
    #4.Definir variable.
    #Mostrar resultado.
########################################################################

#Importar random
import random
#Inicio del juego.
print("¡Bienvenido/a al juego! ¿Te atreves a adivinar en que número estoy pensando? ")
nom = input("¿Cómo te llamas?: ")
#definir rango
num = random.randint(1,100)
num_jugador = int(input("Escribe un número entre 1 y 100: "))
intentos = 1
#definir itentos
while intentos<10:
    print("Tienes 10 intentos, llevas", intentos, "¡Adivínalo!")
    intentos=intentos+1
#Definir variable.
    if num_jugador<num:
        print("Tu número es menor. Prueba de nuevo.")
        num_jugador = int(input("Escribe un número entre 1 y 100: "))
    if num_jugador>num:
        print("Tu número es mayor. Prueba de nuevo.")
        num_jugador = int(input("Escribe un número entre 1 y 100: "))
    if num_jugador==num:
        break
#Mostrar resultado ganador.
if num_jugador==num:
    print("¡Enhorabuena",nom,"!¡Lo has adivinado!")
#Mostrar resultado perdedor.
if num_jugador!=num:
    print("¡Vaya,",nom,"! No ha podido ser esta vez.")