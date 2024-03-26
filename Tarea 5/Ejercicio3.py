#Ejercicio
#Tenemos la siguiente variable definida en nuestro programa (esta variable puede tener cualquier valor, es decir, le podemos añadir nuevas ciudades con temperaturas):
    #temperaturas='''Utrera,29,12
    #Dos Hermanas,32,14
    #Sevilla,30,15
    #Alcalá de Guadaíra,31,14
    #'''
#En esa cadena se definen nombres de poblaciones y las temperaturas máximas y mínimas de dichas poblaciones durante un día.
#Realiza un programa que muestre el nombre de las poblaciones y la temperatura media. 
#Además el programa te debe pedir el nombre de una población y nos debe dar la temperatura máxima y mínima (si la población no existe se debe dar une error.)
#Ayuda: Puede venir muy bien utilizar los métodos splitlines y split de cadenas.
########################################################################

poblacion = ["Dos Hermanas", "Utrera", "Sevilla", "Alcala de Guadaíra", "Bormujos", "Carrión"]
max = [32,29,30,31,33,32]
min = [14,12,15,14,13,14]
localidad = ''
while localidad != 'salir':
    localidad = input("Escriba el nombre de la localidad: ")
    if localidad not in poblacion and localidad != 'salir':
        print("Esa localidad no se encuentra en la lista de datos.")
        nueva = input("¿Desea introducir esa ciudad y sus datos a la lista? (s/n): ")
        while nueva != 's' and nueva !='n':
            nueva = input("Valor incorrecto. Especifíque (s/n): ")
        if nueva == 's':
            nueva_max = int(input("¿Cuál es la temperatura máxima?: "))
            nueva_min = int(input("¿Cuál es la temperatura mínima?: "))
            poblacion.append(localidad)
            max.append(nueva_max)
            min.append(nueva_min)
            print("Ciudad incluida.")
    elif localidad != 'salir':
        posicion = poblacion.index(localidad)
        print ("La localidad", localidad, "tiene una temperatura máxima de %s ºC y una temperatura minima de %d ºC." % (max[posicion], min[posicion]))
else:
    print("Adiós.")