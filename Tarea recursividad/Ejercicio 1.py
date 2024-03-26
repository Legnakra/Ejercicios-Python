#Ejercicio
#Crea una aplicación que pida un número y calcule su factorial 
#(El factorial de un número es el producto de todos los enteros entre 1 y el propio número y se representa por el número seguido de un signo de exclamación. Por ejemplo 5! = 1x2x3x4x5=120).
########################################################################
#Análisis:
    #Problema: Leer un número y calcular su factorial.
    #Entrada: número (real).
    #Salida: contador (entero), resultado (real).
########################################################################
#Diseño:
    #1.Leer número.
    #2.Iniciar cálculo.
    #4.Mostrar resultado.
########################################################################

#1.Leer número
num = int(input("Escriba un número para hallar su factorial: "))
#2.Iniciar cálculo.
def factorial(n): 
    return 1 if (n==1 or n==0) else n * factorial(n - 1); 
#3.Mostrar resultado. 
print("El número factorial de",num,"es", factorial(num),".")