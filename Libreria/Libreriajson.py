import json

#Leer json
def leer_json(fichero):
    try:
        with open(fichero) as f:
            libreria = json.load(f)
        return libreria
    except:
        print("Error al leer el fichero.")

#Contar libros
def contar_libros (libreria):
    return len(libreria.get("bookstore").get("book"))

#Precio intervalo
def seleccionar_por_precio (libreria,preciomin, preciomax):
    libro=libreria.get("bookstore").get("book")
    libros =[]
    for i in libro:
        precio = float(i.get("price"))
        if precio >= preciomin and precio <= preciomax:
            libros.append(i.get("title").get("__text"))
    return libros

#Seleccionar por título
def seleccionar_por_titulo (libreria, cadena):
    libros=[]
    lista = libreria.get("bookstore").get("book")
    for libro in lista:
        if libro.get("title").get("__text").startswith(cadena):
            libros.append((libro.get("title").get("__text").get("year")))
        return libros


#Titulos y autores
def ver_titulos_autores (libreria):
    libros =[]
    autores = []
    lista = libreria.get("bookstore").get("book")
    for libro in lista:
        if isinstance(libro.get("author"), list):
            autores.append(libro.get("author"))
        else:
            autores.append([libro.get("autor")])
            libros.append([libro.get("title").get("__text")])
    return libros, autores