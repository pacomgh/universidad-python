import psycopg2

conexion = psycopg2.connect(user="postgres",
                            password="admin",
                            host="127.0.0.1",
                            port="5432",
                            database="test_db")

cursor = conexion.cursor()
# cada %s tiene un valor asociado a la tabla(nombre, apellido, email)
sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
#usamos una tupla de tuplas para actualizar varios registros
valores = (
    ('Juan', 'Perez', 'jperez@mail.com', 1),
    ('Karla1', 'Gomez2', 'kgomez3@mail.com', 2),
)
#executemany nos permite atualizar varios registros
cursor.executemany(sentencia, valores)
#guardamos la informacion en la bd
conexion.commit()  # la usamos para insert, update, delete para modificar el estado de la bd
#recuperamos la cantidad de registros insertados
registros_actualizados = cursor.rowcount
print(f'registros insertados: {registros_actualizados}')
cursor.close()
conexion.close()
