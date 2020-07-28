""" El objetivo del ejercicio es crear un sistema de calificaciones, como sigue:
El usuario proporcionará un valor entre 0 y 10.
Si está entre 9 y 10: imprimir una A
Si está entre 8 y menor a 9: imprimir una B
Si está entre 7 y menor a 8: imprimir una C
Si está entre 6 y menor a 7: imprimir una D
Si está entre 0 y menor a 6: imprimir una F
cualquier otro valor debe imprimir: Valor desconocido """

calificacion = float(input("Ingresa una calificación(0-10): "))

if calificacion >= 9 and calificacion <= 10:
    print("Tu calificacion es: A")
elif calificacion >= 8 and calificacion < 9:
    print("Tu calificacion es: B")
elif calificacion >= 7 and calificacion <8:
    print("Tu calificacion es: C")
elif calificacion >= 6 and calificacion < 7:
    print("Tu calificacion es: D")
elif calificacion >=0 and calificacion < 6:
    print("Tu calificacion es: F")
else:
    print("Calificación ingresada: ", calificacion ," invalida")


    
