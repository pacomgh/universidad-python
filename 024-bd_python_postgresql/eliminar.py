import psycopg2

conexion = psycopg2.connect(user="postgres",
                            password="admin",
                            host="127.0.0.1",
                            port="5432",
                            database="test_db")

cursor = conexion.cursor()
# cada %s tiene un valor asociado a la tabla(nombre, apellido, email)
sentencia = 'DELETE FROM persona WHERE id_persona=%s'
#insertamos los valores de la tupla
#valores = (8,)
entrada = input("Proporciona la pk a eliminar: ")
valores = (entrada,)
cursor.execute(sentencia, valores)

#guardamos la informacion en la bd
conexion.commit()  # la usamos para insert, update, delete para modificar el estado de la bd
#recuperamos la cantidad de registros insertados
registros_eliminados = cursor.rowcount
print(f'registros eliminados: {registros_eliminados}')
cursor.close()
conexion.close()
