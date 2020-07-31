#Dada la siguiente tupla, crear una lista que sólo incluya los números menor que 5 utilizando un ciclo for:

tupla = (13, 1, 8, 3, 2, 5, 8)
lista = []
for num in tupla:
    if num<5:
        lista.append(num)

i=0
for valor in lista:
    print("valores de la lista: ",valor)
    


