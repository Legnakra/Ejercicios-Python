#Ejercicio2
#El programa pregunta la edad al usuario y almacena la respuesta en la variable "edad". Después comprueba si la edad es inferior a 18 años. 
#Si esta comparación es cierta, el programa escribe que es menor de edad y si es falsa escribe que es mayor de edad. 
#Finalmente el programa siempre se despide, ya que la última instrucción está fuera de cualquier bloque y por tanto se ejecuta siempre.
########################################################################

edad = int(input("¿Cuál es su edad?: "))
if edad < 18:
    print("Usted es menor de edad.")
else:
    print("Eres mayor de edad.")
print("¡Hasta otra!")