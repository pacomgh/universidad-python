#importamos desde dominio la clase pelicula
from dominio.peliculas import Pelicula
from servicio.catalogo_peliculas import CatalogoPeliculas

#variable que controla la opcion a elegir
opcion = None

while opcion != "4":
    print("Opciones")
    print("1. Agregar pelicula")
    print("2. Listar pelicula")
    print("3. Eliminar catalogo")
    print("4. Salir")
    opcion = input("Escribe tu opcion 1-4: ")#guardamos la opcion que elegimos
    if opcion == "1":
        #guardamos el tipo de la pelicula
        nombrePelicula = input("proporciona el nombre de la pelicula: ")
        pelicula = Pelicula(nombrePelicula)
        #llamamos al metodo agregar pelicula y agregamos la pelicula que acaban de ingresa
        CatalogoPeliculas.agregarPelicula(pelicula)
    elif opcion == "2":
        CatalogoPeliculas.listarPeliculas()
    elif opcion == "3":
        CatalogoPeliculas.eliminar()
else:
    print("Salimos del programa")
