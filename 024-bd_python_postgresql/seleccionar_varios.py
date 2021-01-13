import psycopg2

conexion = psycopg2.connect(user="postgres",
                            password="admin",
                            host="127.0.0.1",
                            port="5432",
                            database="test_db")

cursor = conexion.cursor()
entrada = input('Proporciona las pk a buscar (separado por comas): ')
#llamamos a split para separar la entrada y lo convertimos a tupla para solo tener los valores de pk
tupla = tuple(entrada.split(','))#si no usamos split incluiria las ,
print(tupla)
#creamos una tupla de tuplas
llaves_primarias = (tupla,)
#usamos como comodin $s que luego cambiaremos por un valor
sentencia = 'SELECT * FROM persona WHERE id_persona IN %s'#IN proporcionar varios valores(PK)
cursor.execute(sentencia, llaves_primarias) #llave primaria se sustituye en el $s
registros = cursor.fetchall()
for registro in registros:
    print(registro)

cursor.close()
conexion.close()
