#Iterar una lista de 0 a 10  e imprimir sólo los números divisibles entre 3

lista = [0,1,2,3,4,5,6,7,8,9,10]

for num in lista:
    if num%3==0:
        print("numero: ",num," es divisible entre 3 ", num/3)
