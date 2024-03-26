#Ejercicio2
#Escribe un programa que lea números enteros positivos hasta que se introduzca un 0. 
#El programa deberá mostrar por pantalla la cantidad de números leídos, el mayor, el menor y la media de los números leídos.
########################################################################
#Análisis:
    #Problema: Leer números positivos hasta llegar al 0.
    #Entrada: num(entero), mayor(entero), menor(entero), total(entero)
    #Salida: media(real)
########################################################################
#Diseño:
    #1.Leer número.
    #2.Mostrar números leídos.
    #3.Mostrar el mayor, el menor y la media de los números leídos.
    #4.Mostrar resultado.
########################################################################


total=0
mayor=0
menor=0
contador=1
num=int(input("Escriba un número: "))
total+=num
while num != 0:
    num=int(input("Escribe otro número (Pulse 0 para finalizar): "))
    if num !=0:
        contador+=1
    total+=num
    if num>mayor:
        mayor=num
    if num<menor and num !=0:
        menor=num
media = total/contador
print("El número mayor de la consecución es: ",mayor)
print("El número mayor de la consecución es: ",menor)
print("La media de la consecución es: ",media)