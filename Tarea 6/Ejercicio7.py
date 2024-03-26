#Ejercicio
#Realizar una aplicación que recoja por teclado la cantidad total a pagar y la cantidad que se ha entregado. 
#La aplicación debe calcular el cambio correspondiente con el menor número de monedas y/o billetes posibles.
########################################################################

dinero=[50000,20000,10000,5000,2000,1000,500,200,100,50,20,10,5,2,1]
cantidad_total=float(input("Cantidad total a pagar: "))
cantidad_recibida=float(input("Cantidad entregada: "))
devolucion_2=(cantidad_recibida-cantidad_total)
devolucion=round((cantidad_recibida-cantidad_total)*100)
print ("La cantidad a devolver es ", devolucion_2, "€.")
print (" ")

if devolucion/dinero[0]>=1:
	print ("%d Billete de 500 euros" % (devolucion/dinero[0]))
	devolucion=devolucion%dinero[0]
if devolucion/dinero[1]>=1:
	print ("%d Billete de 200 euros" % (devolucion/dinero[1]))
	devolucion=devolucion%dinero[1]
if devolucion/dinero[2]>=1:
	print ("%d Billete de 100 euros" % (devolucion/dinero[2]))
	devolucion=devolucion%dinero[2]
if devolucion/dinero[3]>=1:
	print ("%d Billete de 50 euros" % (devolucion/dinero[3]))
	devolucion=devolucion%dinero[3]
if devolucion/dinero[4]>=1:
	print ("%d Billete de 20 euros" % (devolucion/dinero[4]))
	devolucion=devolucion%dinero[4]
if devolucion/dinero[5]>=1:
	print ("%d Billete de 10 euros" % (devolucion/dinero[5]))
	devolucion=devolucion%dinero[5]
if devolucion/dinero[6]>=1:
	print ("%d Billete de 5 euros" % (devolucion/dinero[6]))
	devolucion=devolucion%dinero[6]
if devolucion/dinero[7]>=1:
	print ("%d moneda de 2 euros" % (devolucion/dinero[7]))
	devolucion=devolucion%dinero[7]
if devolucion/dinero[8]>=1:
	print ("%d moneda de 1 euro" % (devolucion/dinero[8]))
	devolucion=devolucion%dinero[8]
if devolucion/dinero[9]>=1:
	print ("%d moneda de 50 centimos" % (devolucion/dinero[9]))
	devolucion=devolucion%dinero[9]
if devolucion/dinero[10]>=1:
	print ("%d moneda de 20 centimos" % (devolucion/dinero[10]))
	devolucion=devolucion%dinero[10]
if devolucion/dinero[11]>=1:
	print ("%d moneda de 10 centimos" % (devolucion/dinero[11]))
	devolucion=devolucion%dinero[11]
if devolucion/dinero[12]>=1:
	print ("%d moneda de 5 centimos" % (devolucion/dinero[12]))
	devolucion=devolucion%dinero[12]
if devolucion/dinero[13]>=1:
	print ("%d moneda de 2 centimos" % (devolucion/dinero[13]))
	devolucion=devolucion%dinero[13]
if devolucion/dinero[14]>=1:
	print ("%d moneda de 1 centimo" % (devolucion/dinero[14]))
	devolucion=devolucion%dinero[14]