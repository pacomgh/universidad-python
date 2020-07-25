""" alto = int(input("Poporciona el alto del rectangulo "))
ancho = int(input("Poporciona el ancho del rectangulo "))

area = alto * ancho
perimetro = (alto + ancho)*2

print("El area es: ", area)
print("El perimetro es ", perimetro) """

""" Solicitar al usuario dos valores:
    numero1(int)
    numero2(int)
Se debe imprimir el mayor de los dos números 
    Proporciona el numero1:
    Proporciona el numero2:
    El numero mayor es:<numeroMayor>"""

num1 = int(input("Proporciona el numero1: "))
num2 = int(input("Proporciona el numero2: "))

if(num1 > num2):
    numeroMayor = num1
    print("El numero mayor es: ", numeroMayor)
else:
    if(num1 < num2):
        numeroMayor = num2
        print("El numero mayor es: ", numeroMayor)
    else:
        if(num1 == num2):
            print("Los dos numero son iguales")
        
    
