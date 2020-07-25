print("Proporciona los siguientes datos del libro")
nombre = input("Ingresa el nombre del libro: ")
id = int(input("Proporciona el ID del libro: "))
precio = float(input("Proporciona el precio del libro: "))
envioGratuito = input("Ingresa si el envio es gratuito (True/False): ")

if envioGratuito.capitalize() == "True":
    envioGratuito = True
elif envioGratuito.capitalize() == "False":
    envioGratuito=False
else:
    envioGratuito = "Valor incorrecto, debe ser True o False"
    
print("Nombre del libro: ", nombre)
print("ID del libro: ", id)
print("Precio del libro: ", precio)
print("Envio gratuito?: ", envioGratuito)

print(type(envioGratuito))


