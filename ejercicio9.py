"""
Escribe un programa que reciba del usuario nombres y los almacene en una lista.

Otro dato, que reciba apellidos y los guarde en una lista.

Como resultado, el programa generará nuevs nombres mezclando los elementos de las 2 listas.

Ejemplo: Juan Pérez, Maria Del Valle.
"""

import random

nombres = []
apellidos = []

def name():
    
    for i in range(5):
        nombre = input("Introduce un nombre: ")
        nombres.append(nombre)

name()

def last_name():
    
    for i in range(5):
        apellido = input("Introduce un apellido: ")
        apellidos.append(apellido)

last_name()

def select_random(nombres):
    return random.choice(nombres)

print(select_random(nombres))

def select_random(apellidos):
    return random.choice(apellidos)

print(select_random(apellidos))