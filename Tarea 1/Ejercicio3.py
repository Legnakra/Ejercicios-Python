#Ejercicio11
#Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por
#correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de
#los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada
#muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último
#pedido y calcule el peso total del paquete que será enviado. Además se nos pide el precio que se cobra
#por gramo, , y se nos mostrará el total de dinero que necesitamos para realizar el envío.
########################################################################
#Análisis:
#Problema: Tenemos que calcular el peso del último pedido de payasos y muñecas, y el precio por gramo
#al realizar el envío.
    #Entrada: payasos (real), muñecas (real), peso_payaso (real), peso_muñeca (real).
    #Salida:peso_total (real), precio_envío (entero).
#########################################################################
#Diseño:
    #1.Leer cantidad de payasos (payasos)
    #2.Leer cantidad de muñecas (muñecas)
    #3.Calcular el peso del pedido (peso_total = peso_payaso*payaso + peso_muñeca*muñeca)
    #4.Leer el precio del envío por gramo.
    #5.Calcular precio del envío.
    #6.Mostrar el resultado.
#########################################################################

peso_payaso = 112
peso_muñeca = 75
#1.Leer cantidad de payasos (payasos)
payasos = int(input("Introduce el número de payasos a enviar: "))
#2.Leer cantidad de muñecas (muñecas)
muñecas = int(input("Introduce el número de muñecas a enviar: "))
#3.Calcular el peso del pedido (peso_total = peso_payaso*payaso + peso_muñeca*muñeca)
peso_total = peso_payaso * payasos + peso_muñeca * muñecas
#4.Leer el precio del envío por gramo.
precio = float(input("El precio por gramo del envío es de: "))
#5.Calcular precio del envío.
precio_envio = peso_total * precio
#6.Mostrar el resultado.
print("El precio total del envío es de: ",precio_envio,"€." )





