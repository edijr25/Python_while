##Dada una lista de números, imprimir la suma de todos los elementos de la lista.

numeroLista = [1, 2, 3, 4, 5]

i= 0
suma = 0

while i<len(numeroLista):
    suma += numeroLista [i]
    i+= 1

print("La suma de los numeros de la lista es ",suma) 