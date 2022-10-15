"""
Realiza dos listas de números enteros.

Suma el valor de la lista 1 con los valores de la lista 2.

Muestra al usuario el resultado de esta operación.
"""

lista_a = [5,2,6,9,2,1]
lista_b = [1,3,4,9,7,2]

suma_a = sum(lista_a)
print("La suma de la lista_a es: ", suma_a)
suma_b = sum(lista_b)
print("La suma de la lista_b es: ", suma_b)

resultado = suma_a + suma_b

print("La suma total de ambas listas es: ", resultado)