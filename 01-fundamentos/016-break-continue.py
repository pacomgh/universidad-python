#break rompe el ciclo
#imprimir solo las letras a

for letra in "Holanda":
    if letra == "a":
        print(letra)
        #el break termina con el ciclo despues de la primera vez que
        #se encuentra la a
        break
else:
    print("fin del ciclo for")

print("Continua el programa")

#uso de continue
#imprimir los numeros pares dentro de un rango
#range determina un rango de numeros
''' for i in range(6):
    if i%2 == 0:
        print(i) '''
        
#numero diferente de par, que continue a la siguiente iteracion
#continue, que continue con la siguiente iteracion y no ejecute
#las siguiente lineas de codigo
for i in range(6):
    if i % 2 != 0:
        continue
    print(i)
    
