#Ejercicio4
#Escriba un programa que solicite números al usuario hasta que se hayan introducido 10 números o la suma de todos los números leídos sea mayor que 100. 
#A continuación mostrar un mensaje indicando qué condición se ha cumplido (es decir, si se han introducido 10 números o si su suma es mayor que 100)
########################################################################
#Análisis:
    #Problema:Leer números que, cuyo resultado al sumarse, den un valor mayor que 100 o sean 10 números.
    #Entrada: numero (real).
    #Salida: suma (real), contador(entero).
########################################################################
#Diseño:
    #1.Pedir número.
    #2.Comprobar si son 10 números o si su suma es mayor que 100.
    #3.Mostrar resultado.
########################################################################

contador=0
suma=0
while contador<10 and suma<100:
    num=float(input("Escribe un número: "))
    contador=contador+1
    suma=suma+num
if (contador==10):
    print("La suma de los números introducidos es",suma)
    print("La cantidad de números introducida es",contador)
while (suma>100):
    print("La suma de los números introducidos es",suma)
    print("La cantidad de números introducida es",contador)