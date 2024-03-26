#Ejercicio4
#Crear un programa de ordenador para gestionar los resultados de la quiniela de fútbol. Para ello vamos a utilizar dos listas:
    #Equipos: Que es una lista cuyos elementos son una lista con el nombre de los equipos que juegan el partido. En la quiniela se indican 15 partidos.
    #Ejemplo: equipos = [[“Sevilla”,”Betis”],[“Madrid”,”Barcelona”],…]
    #Resultados: Es una lista de enteros donde se indica el resultado. También tiene dos columnas (cada elemento es una lista), 
    #en la primera se guarda el número de goles del equipo que está guardado en la primera columna de la tabla anterior, y en la segunda los goles del otro equipo. 
    #Ejemplo: resultados=[[3,0],[0,0],…]
#El programa ira pidiendo los nombres de los equipos de cada partido y el resultado del partido, a continuación se imprimirá la quiniela de esa jornada.
########################################################################

num_partidos = 15
equipos = []
resultados = []
for indice in range(0,num_partidos):
	partido = []
	partido.append(input("Introduzca el nombre del 1er equipo del partido %d: " % (indice+1)))
	partido.append(input("Introduzca el nombre del 2o equipo del partido %d: " % (indice+1)))
	equipos.append(partido)
	goles = []
	goles.append(int(input("¿Cuántos goles ha metido el %s?: " % (partido[0]))))
	goles.append(int(input("¿Cuántos goles ha metido el %s?: " % (partido[1]))))
	resultados.append(goles)
print ("- - - - - - - - - - - - - - - - - - ") 
print ("Los resultados de la quiniela son: ")
print ("- - - - - - - - - - - - - - - - - - ")    

for partido,goles in zip(equipos,resultados):
	print(partido[0],"-",partido[1],":",end="")
	if goles[0] > goles[1]:
		print("-> 1")
	else:
		if goles[0] < goles[1]:
			print("=> 2")
		else:
			print("=> X")