# Pedir una cadena de caracteres
# Averiguar que caracteres no están repetidos y mostrarlos por pantalla.
cadena = str(input("Introduce caracteres: "))
cadena = ''.join(cadena.split(' '))
no_repetidos = []
for caracter in cadena:
    cadena.count(caracter)
    if cadena.count(caracter) == 1:
        if not caracter in no_repetidos:
            no_repetidos.append(caracter)
if no_repetidos == []:
    print("No existen caracteres únicos.")
else:
    ordenados = sorted(no_repetidos)
    print('Caracteres no repetidos: ')
    print(ordenados)