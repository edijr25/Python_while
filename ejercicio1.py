##Dado un número entero n, imprimir todos los números desde n hasta 1 en orden descendente.

n = int(input("Ingrese un número entero: "))

i = n

while i >= 1:
    print(i)
    i -= 1