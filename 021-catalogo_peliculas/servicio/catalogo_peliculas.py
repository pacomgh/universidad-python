import os
class CatalogoPeliculas:
    #esta es una variable estatica
    rutaArchivo = "universidad_python/021-catalogo_peliculas/peliculas.tx"
    #convierte al metodo en un metodo estatico, no recibe ningun parametro self,cls
    #podemos recibir otro tipo de parametros
    @staticmethod#decorador
    def agregarPelicula(pelicula):#recibimos un objeto de tipo pelicula
        try:
            #abrimos archivo, en el modo append "a"
            archivo = open(CatalogoPeliculas.rutaArchivo, "a")
            #convertimos el objeto pelicula a un string para poder mandarlo al archivo
            archivo.write(pelicula.__str__())            
        except Exception as e:
            print("Ocurrio una excepcion al agregar: ", e)
        finally:
            archivo.close()
            
    @staticmethod
    def listarPeliculas():
        try:
            archivo = open(CatalogoPeliculas.rutaArchivo, "r")
            print("Catalogo de peliculas: ")
            print(archivo.read())
        except Exception as e:
            print("Ocurrio un error al listar pelciulas: ", e)
        finally:
            archivo.close()
            
    @staticmethod
    def eliminar():
        try:
            os.remove(CatalogoPeliculas.rutaArchivo)
            print("archivo eliminado: ", CatalogoPeliculas.rutaArchivo)
        except Exception as e:
            print("Ocurrio un error al eliminar peloculas: ", e)
    
