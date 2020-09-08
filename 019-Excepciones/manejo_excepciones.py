from numeros_identicos import NumerosIdenticosException
resultado = None
#a="10"
#b=0
#En el manejo de excepciones primero ponemos la excepcion de menor jerarquia
try:
    a = int(input("Primer numero: "))
    b = int(input("Segundo numero: "))
    if a==b:
        #lanzamos la excepcion que creamos con raise, esta excepcion solo es conocida
        #por la clase padre Excepction que es la que la va a cachar
         raise NumerosIdenticosException("Numeros identicos")
    resultado = a/b
#para saber el tipo de excepcion
except ZeroDivisionError as e:
    print("Ocurrio un error con ZeroDivisionError:", e)
    #tipo de excepcion
    print(type(e))
except TypeError as e:
    print("Ocurrio un error con TypeError:", e)
    print(type(e))   
#except ValueError as e:
#    print("Ocurrio un error con ValueError:", e)
#    print(type(e))
except Exception as e:#aqui se procesa nuestra excepcion
    print("Ocurrio un error con Exception:", e)
    print(type(e))  
#cuando no hay ninguna excepcion
else:
    print("No hubo ninguna excepcion")
finally:#opcional agregarlo, siempre se ejecuta
    print("Fin del manejo de excepciones")    
    
    
print("resultado", resultado)
#si queremos seguir ejecutando el programa continua sin problema, sin excepcion
#termina el programa
print("continuamos...")
