import psycopg2

conexion = psycopg2.connect(user="postgres",
                            password="admin",
                            host="127.0.0.1",
                            port="5432",
                            database="test_db")
try:
    #autocommit hace que se envien todas las transacciones
    #conexion.autocommit = True
    cursor = conexion.cursor()
    # cada %s tiene un valor asociado a la tabla(nombre, apellido, email)
    sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES (%s, %s, %s)'
    #insertamos los valores de la tupla
    valores = ('Maria', 'Esparza', 'mesparza@mail.com')
    cursor.execute(sentencia, valores)

    sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
    #insertamos los valores de la tupla
    valores = ('Juan1', 'Perez2', 'jperez3@mail.com', 1)
    cursor.execute(sentencia, valores)

    ###si falla alguna transaccion no se guarda ningun cambio, es todos o nada

    #guardamos la informacion en la bd, el commit siempre va al final de todas las transacciones
    conexion.commit()  # la usamos para insert, update, delete para modificar el estado de la bd

except Exception as e:#cuando ocurre una excepcion se hace un rollback
    #rollback da marcha atras a todas las operaciones pendientes
    conexion.rollback()
    print(f"Ocurrio un error en la transaccion")
finally:#en cualquier caso se cierra el cursor y la conexion
    cursor.close()
    conexion.close()
