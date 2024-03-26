#Ejercicio
#Para calcular la letra del DNI se calcula el número del DNI módulo 23 y el resultado es la posición en la siguiente cadena:
#Crear un programa que pida un DNI (valide que tiene 9 caracteres) y diga si es válido.
########################################################################
#Análisis:
    #Problema:Mostrar en pantalla la letra correspondiente al número de DNI introducido.
    #Entrada: dni(real), letras (entero), valor(entero)
    #Salida: letra (entero)
########################################################################
#Diseño:
    #1.Establecer método de extración de letra.
    #2.Calcular la letra.
    #3.Mostrar resultado.
########################################################################

letras = "TRWAGMYFPDXBNJZSQVHLCKE"
numeros = "1234567890"
dni = input("Introduce el NIF: ")
while (len(dni) != 9):
    print("DNI incorrecto. Vuelva a introducirlo.")
    dni = input("Introduce el NIF: ")
letra_usuario = dni[8].upper()
numeros_usuario = dni[:8]
while not numeros_usuario.isdigit() or not letra_usuario.isalpha():
    print("DNI incorrecto. Vuelva a introducirlo.")
    dni = input("Introduce el NIF: ")
while letras[int(numeros_usuario)%23] != letra_usuario:
    print("DNI incorrecto. Vuelva a introducirlo.")
    dni = input("Introduce el NIF: ")
    letra_usuario = dni[8].upper()
    numeros_usuario = dni[:8]
else:
    print("DNI correcto.")