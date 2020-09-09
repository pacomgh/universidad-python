#si no existe crea el archivo en la ruta que seleccionamos
#el parametro es el modo con el que trabajaremos
try:
    #archivo = open("universidad_python/020-archivos/prueba.txt", "w")
    archivo = open("prueba.txt", "w")
    #agregamos info por el metodo write
    archivo.write("agregamos info al archivo\n")
    archivo.write("Adios")
except Exception as e:
    print(e)
finally:#siempre se va a cerrar este archivo con el finally
    archivo.close()
    #despues de cerrar el archivo ya no podemos trabajar con el
