#Ejercicio4
#Programa que pide un valor y nos dice:
    #si es múltiplo de dos,
    #si es múltiplo de cuatro (y de dos)
    #si no es múltiplo de dos
########################################################################

numero = int(input("Escriba un número: "))
if numero %2 ==0:
    print(f"{numero} es múltiplo de 2.")
elif numero % 4 ==0:
    print(f"{numero} es múltiplo de 4 y de 2.")
else:
    print(f"{numero} no es múltiplo de 2.")