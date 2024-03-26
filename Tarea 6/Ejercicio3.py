#Ejercicio3
#Queremos hacer un programa que trabaje con las notas de los alumnos de una clase:
    #El programa pedirá cuantos alumnos tiene la clase.
    #A continuación, pedirá el nombre del alumno, y cuantas notas tiene ese alumno.
    #Se pedirán las notas del alumno introducido (cada alumno puede tener una cantidad de notas distintas). Las notas se validarán para que sea un número del 1 al 10).
#Piensa en el estructura de datos donde vas a guardar la información. Al finalizar el programa nos mostrará el siguiente menu:
    #Notas medias: Nos muestra una lista de alumnos y su nota media. Si su nota media es aprobado aparecerá la palabra “APROBADO” en la línea del alumno.
    #Buscar por nombre: Nos pide una cadena y nos muestra todos los alumnos que **comienzan por dicha cadena y la lista de sus notas.
    #Añadir alumno: No pide el nombre de un alumno, cuántas notas tienes y pide las notas.
    #Eliminar alumno: Nos pide un nombre y elimina el primer alumno que encuentre con ese nombre.
    #Salir
########################################################################

lista_alumnos = {}
existe = 0
num_alumnos = int(input("¿Cuántos alumnos va a introducir?: "))
for num in range(num_alumnos):
    alumno = input("Escriba el nombre del alumno: ")
    while alumno in lista_alumnos:
        print("Este alumno ya existe.")
        alumno = input("Escriba el nombre del alumno: ")
    notas=[]
    nota = int(input("Escriba la nota del alumno (Introduzca un número negativo para finalizar):"))
    while nota > 0:
        notas.append(nota)
        nota = int(input("Escriba la nota del alumno (Introduzca un número negativo para finalizar):"))
    lista_alumnos[alumno] = notas.copy()
print("\n")
print("- - - - - - - - - - - - - - - - - - - - - - - ")
print("1. Notas medias.")
print("2. Buscar por nombre.")
print("3. Añadir alumno.")
print("4. Eliminar alumno.")
print("0. Salir.")
print("- - - - - - - - - - - - - - - - - - - - - - - ")
opcion = int(input("Elija una opción: "))
while opcion !=0:
    #Notas medias
    if opcion ==1:
        for nom_alumno, lista_notas in lista_alumnos.items():
            media = sum(lista_notas)/len(lista_notas)
            if media >=5:
                print("El alumno %s tiene una nota media de %f" % (nom_alumno,media),". APROBADO.")
            else:
                print("El alumno %s tiene una nota media de %f" % (nom_alumno,media))
    #Buscar por nombre
    elif opcion ==2:
        cadena=input("Escriba el alumno que desea buscar: ")
        for alumno,notas in lista_alumnos.items():
            if alumno.startswith(cadena):
                existe=1
                print("Las notas del alumno %s son: %s "% (alumno,notas))
        if existe == 0:
                print("No se encuentra coincidencias.")
    #Añadir alumno
    elif opcion ==3:
        notas=[]
        alumno = input("Introduzca el nombre del alumno que desea añadir: ")
        nota = int(input("Escriba la nota del alumno (Introduzca un número negativo para finalizar):"))
        notas.append(nota)
        while nota > 0:
            nota = int(input("Escriba la nota del alumno (Introduzca un número negativo para finalizar):"))
            if nota >0:
                notas.append(nota)
            lista_alumnos[alumno] = notas.copy()
        print (lista_alumnos)
    #Eliminar alumno
    elif opcion == 4:
        del_alumno = input("Nombre del alumno que se desea borrar: ")
        if del_alumno in lista_alumnos:
            seguridad = input("¿Desea borrar el contacto seleccionado? (Presione s para confirmar). ")
            if seguridad == "s":
                del lista_alumnos[alumno]
        print (lista_alumnos)
    print("- - - - - - - - - - - - - - - - - - - - - - - ")
    opcion = int(input("Elija una opción: "))
    print("- - - - - - - - - - - - - - - - - - - - - - - ")
else:
    print("Adiós.")
