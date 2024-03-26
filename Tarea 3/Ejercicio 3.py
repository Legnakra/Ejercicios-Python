#Ejercicio3
#Escriba un programa que pida al usuario su nombre y contraseña y le de tres oportunidades para introducir los datos correctos, que serán root y 1234. 
#Si los datos introducidos son correctos se mostrará por pantalla “Bienvenido al sistema”. 
#En caso contrario se mostrará un mensaje por pantalla indicando que se ha superado el número de intentos permitido.
########################################################################
#Análisis:
    #Problema: Pedir contraseña y usuario, con solo 3 oportunidades para introducir los datos correctos.
    #Entrada: usuario (cadena), contraseña (entero)
    #Salida: user_ok(entero), pass_ok(entero), intentos (entero)
########################################################################
#Diseño:
    #1.Pedir usuario.
    #2.Pedir contraseña.
    #3.Mostrar bienvenida.
    #4.Mostrar error.
########################################################################

user_ok=0
pass_ok=0
intentos=3
while intentos>0:
    usuario=str(input("Escriba su nombre de usuario: "))
    if usuario=='root':
        print("Usuario correcto.")
        user_ok=1
        contraseña=str(input("Escriba su contraseña: "))
        if str(contraseña)=='1234':
            print("Contraseña correcta.")
            pass_ok=1
            break
        else:
            intentos=intentos-1
            if intentos==0:
                print("Ha agotado sus intentos.")
                break
            else:
                print("Contraseña incorrecta. Pruebe de nuevo.Le quedan ",intentos)
    else:
        intentos=intentos-1
        if intentos==0:
            print("Ha agotado sus intentos.")
            break
        else:
            print("Usuario incorrecto. Pruebe de nuevo.Le quedan ",intentos) 
if user_ok==1 and pass_ok==1:
    print("Bienvenido/a al sistema.")