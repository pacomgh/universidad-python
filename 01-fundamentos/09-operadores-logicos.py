#a=int(input("proporciona un valor: "))
a=3
valorMinimo=0
valorMaximo=5

dentroRango=(a>=valorMinimo and a<=valorMaximo)

print(dentroRango)

if(dentroRango):
    print("Esta dentro del rango")
else:
    orint("Esta fuera del rango")

vacaciones = True
diaDeDescanso = False

if(vacaciones or diaDeDescanso):
    print("Podemos ir al parque")
else:
    print("Tienes deberes que hacer")
    
print(not(vacaciones))
