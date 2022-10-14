"""
Realiza un programa que guarde 10 palabras en una lista.

El programa deberá determinar si las palabras de la lista son palíndromos.

Un palindromo es una palabra que al derecho y al revés se escribe igual.

Ejemplo: ana, oso.
"""

def es_palindromo(lista):
    for x in lista:
        if x == str(x)[::-1]:
            print(x, str(x)[::-1], 'Es palíndromo')
        else:
            print(x, str(x)[::-1], 'No es palíndromo')

lista = ["ana", "perro", "oso", "calle", "radar", "valle", "ama", "ola", "nadan", "reir"]

es_palindromo(lista)