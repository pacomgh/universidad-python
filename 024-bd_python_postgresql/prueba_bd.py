# instalalr postgresql pip install psycopg2
# comprobar que se instalo -> consola python -> import pyscopg2 -> enter(no manda error)
# en caso de usar mysql pip install mysql-connector
import psycopg2

# usamos el modulo psycopg2 para conectarnos a la bd con las credenciales indicadas
conexion = psycopg2.connect(user="postgres", 
                 password="admin", 
                 host="127.0.0.1",
                 port="5432",
                 database="test_db")

#pedimos el metodo cursor, este objeto permite ejecutar sentencias sobre la bd
cursor = conexion.cursor()
sentencia = 'SELECT * FROM persona'
#ejecutamos la sentencia sql
cursor.execute(sentencia)
#recuperamos la informacion del cursor
registros = cursor.fetchall()#regresa un diccionario
print(registros)

#Cerramos el cursor y la conexcion a la BD
cursor.close()
conexion.close()
