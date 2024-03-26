#Ejercicio1
#Escriba un programa que pida el año actual y un año cualquiera y que escriba cuántos años han pasado desde ese año o cuántos años faltan para llegar a ese año. 
#Se puede mejorar el programa haciendo que cuando la diferencia sea exactamente un año y escriba la frase en singular.
########################################################################
#Análisis:
    #Problema: Pedir año actual, año cualquiera y mostrar diferencia entre años.
    #Entrada: año1 (real), año2 (real). 
    #Salida: diferencia (real)
########################################################################
#Diseño:
    #1.Pedir año actual y año cualquiera.
    #2.Identificar si son mayor, menor o igual.
    #3.Mostrar resultado.
########################################################################

#1.Pedir año actual y año cualquiera.
año1= int(input("¿En qué año estamos?: "))
año2= int(input("Escriba un año cualquiera: "))
#2.Identificar si son mayor, menor o igual.
if año1<año2:
    diferencia= año2-año1
#3.Mostrar resultado.
    print("Para llegar al año",año2,"faltan",diferencia,"años.")
elif año1>año2:
    diferencia= año1-año2
#3.Mostrar resultado.
    print("Desde el año",año2,"han pasado",diferencia,"años.")
elif año1 ==año2:
#3.Mostrar resultado.
    print("¡Son el mismo año!")