"""
Escribe un programa que guarde 10 números en una lista.

El programa deberá impimir los números de forma ascendente,
y luego de forma descendente.

Consejo: Puedes utilizar las funciones sort(), y reverse()
"""

def validar_numeros(message):
    
    while True:
        try:
            data = int(input("Ingresa " + message))
            return data
        except ValueError:
            print("El dato debe ser un número entero.")

lista_numeros = []

def numeros_asc():
    
    for n in range(10):
        numero = validar_numeros("un número: ")
        lista_numeros.append(numero)

numeros_asc()

lista_numeros.sort()

print("Los números de menor a mayor son: \n")
for a in lista_numeros:
    print(a)

lista_numeros.reverse()

print("Los números de mayor a menor son: \n")
for d in lista_numeros:
    print(d)