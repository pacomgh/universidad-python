import psycopg2

conexion = psycopg2.connect(user="postgres",
                            password="admin",
                            host="127.0.0.1",
                            port="5432",
                            database="test_db")

cursor = conexion.cursor()
#id_persona=1
id_persona = input('Proporciona la pk a buscar: ')
#convertimos la variable en una tupla para los valores que se recuperan
llave_primaria = (id_persona,) #agregamos la , para indicar que es una tupla
#usamos como comodin $s que luego cambiaremos por un valor
sentencia = 'SELECT * FROM persona WHERE id_persona = %s'
cursor.execute(sentencia, llave_primaria) #llave primaria se sustituye en el $s
registros = cursor.fetchone()
print(registros)

cursor.close()
conexion.close()
