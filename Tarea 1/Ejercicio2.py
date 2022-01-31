#Ejercicio2
#Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de
#masa corporal y lo almacene en una variable, e imprima por pantalla la frase “Tu índice de masa corporal es...” y el resultado.
########################################################################
#Análisis:
    #Problema: Tenemos que calcular el IMC (índice de masa corporal) dados el peso (kg) y la estatura (m).
    #Entrada: peso (entero), estatura (entero).
    #Salida: imc (entero).
#########################################################################
#Diseño:
    #1.Leer peso (peso) y estatura (estatura).
    #2.Calcular el IMC (imc = peso/(estatura**2,2).
    #3.Mostrar el resultado.

########################################################################

#1.Leer peso (peso) y estatura (estatura).
peso = input("¿Cuál es tu peso?(kg): ")
estatura = input("¿Cuál es tu estatura (metros): ")
#2.Calcular el IMC (imc = peso/(estatura**2,2).
imc = round(float(peso)/float(estatura)**2,2)
#3.Mostrar el resultado.
print("Tu índice de masa corporal es " + str(imc))