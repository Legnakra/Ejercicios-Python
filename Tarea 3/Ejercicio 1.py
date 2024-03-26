#Ejercicio1
#Escribe un programa que le pida al usuario dos enteros, de manera que el primero sea menor que el segundo, sino se cumple esta condición los volveremos a pedir hasta que se cumpla. 
#Una vez introducidos correctamente mostraremos la suma de todos los enteros comprendidos entre ambos números incluidos ellos. Por ejemplo para los números 3 y 7, la suma seria 25.

########################################################################
#Análisis:
    #Problema: Leer dos números enteros, siendo el primero menor que el segundo, y sumarlos.
    #Entrada: num1 (entero), num2(entero).
    #Salida: resultado (entero).
########################################################################
#Diseño:
    #1.Leer dos números enteros.
    #2.Identificar que el primero sea menor que el segundo.
    #3.Sumar ambos números.
    #4.Mostras resultado.
########################################################################

#1.Leer dos números enteros.
print("Escribe dos números, siendo el primero menor que el segundo.")
num1 = int(input("Escribe el primer número: "))
num2 = int(input("Escribe el segundo número: "))
#2.Identificar que el primero sea menor que el segundo.
while num1>num2:
    print("Recuerda: El primer número debe ser más pequeño que el segundo. Vuelve a intentarlo.")
    num1 = int(input("Escribe el primer número: "))
    num2 = int(input("Escribe el segundo número: "))
else:
    resultado=0
while True:
    if num1<num2:
        break
resultado=0
for i in range(num1,num2+1):
    resultado+=i
print("La suma de los números comprendidos entre ",num1, "y ",num2, "es: ",resultado)