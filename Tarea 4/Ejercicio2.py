#Ejercicio
#Juego de las multiplicaciones.
    #Apartado1:Apartado 1: Escriba un programa que genere una multiplicación de dos números del 2 al 10 al azar, pregunte por el resultado y diga si se ha dado la respuesta correcta.
########################################################################
#Análisis:
    #Problema:Multiplicar dos numeros elejidos al azar
    #Entrada: entrada
    #Salida:
########################################################################
#Diseño:
    #1.Generar número aleatorio 2 veces
    #2.
    #3.
########################################################################
from random import randint
def main():
    print("Número de preguntas: 0")
preguntas = int(input("Número de preguntas: "))
if preguntas<1:
    print("El número de preguntas debe ser al menos de 1.")
else:
    correcta = 0.0
    for _ in range(preguntas):
        a = randint(2,10)
        b = randint(2,10)
        respuesta = int(input("¿Cuanto es {} x {}?: ".format(a,b)))
        if respuesta == (a*b):
            print("¡Respuesta correcta!")
            correcta+=1
        else:  
            print ("¡Respuesta incorrecta!")
    if correcta ==1:
        print("Ha contestado correctamente 1 pregunta.")
    else:
        print("Ha contestado correctamente ",correcta,)
    nota = round(correcta/preguntas * 10, 1)
    print("Le conrresponde una nota de ",nota)
    if nota >=9:
        print("¡Enhorabuena!")