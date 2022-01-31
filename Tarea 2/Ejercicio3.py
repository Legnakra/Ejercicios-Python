#Ejercicio3
#Programa que pide la edad y en función del valor recibido da un mensaje diferente. Podemos distinguir, por ejemplo, tres situaciones:
    #si el valor es negativo, se trata de un error.
    #si el valor está entre 0 y 17, se trata de un menor de edad.
    #si el valor es superior o igual a 18, se trata de un menor de edad.
########################################################################

edad = int(input("¿Qué edad tiene?: "))
if edad >= 18:
    print("Usted es mayor de edad.")
elif edad < 0:
    print("La edad negativa no existe.")
else:
    print("Usted es menor de edad.")