#Ejercicio5
#Suponiendo que una paella se puede cocinar exclusivamente con arroz y gambas, y que para cada
#cuatro personas se utiliza medio kilo de arroz y un cuarto de kilo de gambas, escribir un programa
#que pida por pantalla el número de comensales para la paella, el precio por kilo de los ingredientes y
#muestre las cantidades de los ingredientes necesarios y el coste de la misma.
########################################################################
#Análisis:
#Problema:Te pide el número de comensales para calcular el precio por kilo de los ingredientes para una paella, muestre las cantidades y el coste de la misma.
    #Entrada: comensales (real), cantidad_arroz (entero), cantidad_gambas (entero), precio_gamba(entero),precio_arroz(entero).
    #Salida:coste_paella (entero).
#########################################################################
#Diseño:
    #1.Leer el número de comensales.
    #2.Calcular ingredientes necesarios para la paella.
    #3.Leer precios del arroz y las gambas.
    #4.Calcular el coste total de la paella.
    #5.Mostrar resultado.
#########################################################################

#1.Leer el número de comensales.
comensales = float(input("El número total de comensales es: "))
#2.Calcular ingredientes necesarios para la paella.
cantidad_arroz= comensales* 0.5/4
cantidad_gambas=comensales* 0.25/4
print("Vamos a necesitar ",cantidad_arroz, "gramos de arroz.")
print("Vamos a necesitar ",cantidad_gambas, "gramos de gambas.")
#3.Leer precios del arroz y las gambas.
precio_arroz= float(input("El precio del arroz(kg) es de: "))
precio_gamba= float(input("El precio de las gambas(kg) es de: "))
#4.Calcular el coste total de la paella.
coste_paella= (cantidad_arroz*precio_arroz)+(cantidad_gambas*precio_gamba)
#5.Mostrar resultado.
print("La paella cuesta: ",coste_paella, "€.")