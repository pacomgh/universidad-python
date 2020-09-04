try:
    10/0
#para saber el tipo de excepcion
except Exception as e:
    print("Ocurrio un error:", e)
    
#si queremos seguir ejecutando el programa continua sin problema, sin excepcion
#termina el programa
print("continuamos...")