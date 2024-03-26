#Ejercicio5
#Escriba un programa que permita calcular el importe de una factura, a partir de una serie de artículos vendidos. 
#Para ello, el programa irá preguntando para cada  artículo la cantidad de unidades vendidas y el precio unitario. 
#El programa comprobará que tanto el precio como la cantidad son números positivos, y en caso  contrario volverá a solicitar los valores. 
#La lectura de artículos acabará cuando se introduzca un 0 en la primera pregunta. Entonces se imprimirá por pantalla el importe total de la factura.
########################################################################
#Análisis:
    #Problema: Leer el importe de una factura. Cerrar el programa al escribir 0.
    #Entrada: precio (real), cantidad(real).
    #Salida: total(real).
########################################################################
#Diseño:
    #1.Pedir cantidad del artículo.
    #2.Pedir precio del artículo.
    #3.Mostrar importe total de la factura.
########################################################################


cantidad=float(input("Intruduzca la cantidad del artículo vendido: "))
total =0
while cantidad>0 or cantidad<0:    
    while cantidad<0:
        print("La cantidad no es correcta.")
        cantidad=float(input("Intruduzca la cantidad del artículo vendido: "))
    else:
        precio=float(input("Intruduzca el precio/unidad del artículo vendido: "))
        while precio<0:
            print("El precio no es correcto.")
            precio=float(input("Intruduzca el precio/unidad del artículo vendido: "))
        else:
            total+=(precio*cantidad)
            cantidad=float(input("Intruduzca la cantidad del artículo vendido: "))
else:
    if total>0:
        print("El total de su factura es: ",total,"€. Gracias por su compra.")
    else:
        print("Programa cerrado.")