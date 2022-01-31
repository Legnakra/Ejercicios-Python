#Ejercicio4
#Diseñar el algoritmo correspondiente a un programa que pida el total de kilómetros recorridos, el
#precio de la gasolina (por litro), el consumo del coche (litros/100 km) y nos muestre la siguiente
#información:
    #El total de litros de gasolina que ha gastado en el trayecto.
    #¿Cuánto dinero te ha costado la gasolina?
########################################################################
#Análisis:
#Problema:Tenemos que calcular el consumo de un coche, el consumo en un recorrido con determinados kilómetros y el coste del trayecto.
    #Entrada:kilometros_recorridos (entero), precio_gasolina (entero), consumo_coche (entero).
    #Salida: total_litros (entero), consumo_gasolina (entero), gasto_gasolina (entero).
#########################################################################
#Diseño:
    #1.Leer kilómetros totales recorridos.
    #2.Leer precio gasolina.
    #3.Leer consumo del coche.
    #4.Calcular litros consumidos en el recorrido.
    #5.Calcular coste de gasolina en el recorrido.
    #6.Mostrar resultado.
#########################################################################

#1.Leer kilómetros totales recorridos.
kilometros_recorridos = float(input("Los kilómetros recorridos son: "))
#2.Leer precio gasolina.
precio_gasolina = float(input("El precio de la gasolina (por litro) es: "))
#3.Leer consumo del coche.
consumo_coche= float(input("El coche consume (litros/100km): "))
#4.Calcular litros consumidos en el recorrido.
consumo_gasolina =consumo_coche / 100 * kilometros_recorridos
print("El coche ha gastado en ",kilometros_recorridos," un total de",consumo_gasolina,"litros de gasolina.")
#5.Calcular coste de gasolina en el recorrido.
gasto_gasolina = consumo_gasolina*precio_gasolina
#6.Mostrar resultado.
print("El gasto total de gasolina es de: ",gasto_gasolina,"€.")