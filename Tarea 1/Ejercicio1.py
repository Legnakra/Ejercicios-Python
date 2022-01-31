#Ejercicio1
#Diseñar el algoritmo correspondiente a un programa que lea el valor correspondiente a una distancia en millas marinas y las escribas expresadas en metros.
########################################################################
#Análisis:
    #Problema: Tenemos que leer una cantidad de millas marinas y calcular su valor en metros.
    #Entrada: millas(entero).
    #Salida: metros (entero).
########################################################################
#Diseño:
    #1. Leer distancia_millas (distancia_millas).
    #2. Convertir millas marinas a metros (distancia_millas*1852).
    #3. Mostrar el resultado.
########################################################################

#1. Leer distancia_millas (distancia_millas).
distancia_millas = float(input("Distancia en millas marinas: "))
#2. Convertir millas marinas a metros (distancia_millas*1852).
metros= distancia_millas*1852
#3. Mostrar el resultado en metros.
print("La distancia en metros es de: ",metros, "metros")
