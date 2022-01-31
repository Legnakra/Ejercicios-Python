#Ejercicio
#Escriba un programa que simule el juego Piedra, papel, tijera para dos jugadores. El programa pide dos cadenas (PIEDRA, PAPEL o TIJERAS) para cada uno de los jugadores.
#Las reglas del juego son las siguientes:
    #El jugador que ha sacado Piedra gana al jugador que ha sacado Tijera.
    #El jugador que ha sacado Tijera gana al jugador que ha sacado Papel.
    #El jugador que ha sacado Papel gana al jugador que ha sacado Piedra.
    #Si los dos sacan el mismo objeto es un empate.
########################################################################

import random

while True:
    aleatorio = random.randrange (0,3)
    elijeUsuario1 = ""
    print("1.Piedra")
    print("2.Papel")
    print("3.Tijera")
    opcion = int(input("Elige: "))

    if opcion ==1:
        elijeUsuario1 = "Piedra"
    elif opcion ==2:
        elijeUsuario1 = "Papel"
    elif opcion ==3:
        elijeUsuario1 = "Tijera"
    print("El jugador ha elegido: ",elijeUsuario1)

    if aleatorio ==1:
        elijeUsuario2 = "Piedra"
    elif aleatorio ==2:
        elijeUsuario2 = "Papel"
    elif aleatorio ==3:
        elijeUsuario2 = "Tijera"
    print("El ordenador ha elegido: ",elijeUsuario2)
    print("...")

    if elijeUsuario1 == "Piedra" and elijeUsuario2 == "Papel":
        print("¡Ganas! Papel envuelve Piedra.")
    elif elijeUsuario1 == "Papel" and elijeUsuario2 == "Tijera":
        print("¡Ganas! Tijera corta Papel.")
    elif elijeUsuario1 == "Tijera" and elijeUsuario2 == "Piedra":
        print("¡Ganas! Piedra destruye Tijera.")
    if elijeUsuario1 == "Papel" and elijeUsuario2 == "Piedra":
        print("¡Oh oh! Has perdido. Papel envuelve a piedra. Suerte la próxima vez")
    elif elijeUsuario1 == "Tijera" and elijeUsuario2 == "Papel":
        print("¡Oh oh! Has perdido. Tijera corta Papel. Suerte la próxima vez")
    elif elijeUsuario1 == "Piedra" and elijeUsuario2 == "Tijera":
        print("¡Oh oh! Has perdido. Piedra machaca a Tijera. Suerte la próxima vez")
    elif elijeUsuario1 == elijeUsuario2:
        print("¡Empate!")