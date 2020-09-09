#utilizamos el modo r para leer archivo
#archivo = open("universidad_python/020-archivos/prueba.txt", "r")#ruta relativa
#ruta absoluta para windows
#archivo = open("E:\\Documentos\\udemy\\universidad_python\\020-archivos\\prueba.txt", "r")
archivo = open("prueba.txt", "r")

#print(archivo.read())
#leer algunos caracteres
#print(archivo.read(5))#leemos 5 caracteres
#leemmos los siguientes tres caracteres
#print(archivo.read(3))
#leemos lineas completas
#print(archivo.readline())
#print(archivo.readline())
#iterando para leer lineas
#for linea in archivo:
#    print(linea)
#leer todas las lineas del archivo
#print(archivo.readlines())#regresa una lista con todas las lineas del archivo
#acceder a una linea de la lista
#print(archivo.readlines()[0])#[indice] de la linea

#copiar un archivo en otro, w+ es para escritura y lectura de informacion
#archivo2 = open("copia.txt", "w+")
#anexa la nueva informacion con a de append
#archivo2 = open("copia.txt", "a")
#sobreescribe el contenido
archivo2 = open("copia.txt", "w")
#en el archivo2 escribimos todo lo leido en el archivo
archivo2.write(archivo.read())
archivo.close()
archivo2.close()
