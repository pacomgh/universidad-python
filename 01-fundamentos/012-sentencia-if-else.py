condicion = 10
#operador ternario
#Se recomienda usar cuando la primera parte es muy breve
print("La condicion es verdadera") if condicion else print(
    "la condicion es falsa")

if condicion == True:
    print("La condicion es verdadera")
elif condicion == False:
    print("la condicion es falsa")
else:
    print("Condicion no reconocida")

numero = int(input("Ingresa un numero entre 1 y 3: "))

if numero == 1:
    numeroTexto = "numero uno"
elif numero == 2:
    numeroTexto = "numero dos"
elif numero == 3:
    numeroTexto = "numero tres"
else:
    numeroTexto = "valor fuera de rango"
    
print("El valor del numero es: " + numeroTexto)
