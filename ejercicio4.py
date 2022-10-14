"""
Escribe un programa que guarde 3 asignaturas en una lista.
3 nombres en otra lista y 3 calificaciones en una tercera lista.

El programa deberá combinar los elementos de las 3 listas,
una impresión podría ser:

El alumno Carlos sacó 7.5 en Inglés.
"""

def validar_nombres(message):
    
    while True:
        try:
            data = input("Ingresa " + message)
            return data
        except ValueError:
            print("El dato debe ser texto.")

def validar_notas(message):
    
    while True:
        try:
            data = float(input("Ingresa " + message))
            return data
        except ValueError:
            print("El dato debe ser entero o decimal.")

nombres = []
asignaturas = []
calificaciones = []

def calificacion():
    
    for n  in range(3):
        nombre = validar_nombres("el nombre del alumno: ")
        nombres.append(nombre)
    for a in range(3):
        asignatura = validar_nombres("la asignatura: ")
        asignaturas.append(asignatura)
    for c in range(3):
        nota = validar_notas("su calificación: ")
        calificaciones.append(nota)

calificacion()

print('')

print("Los nombres de los alumnos son: \n")
for n in nombres:
    print(n)

print('')

print("Las materias son: \n")
for a in asignaturas:
    print(a)

print('')

print("Las calificaciones son: \n")
for c in calificaciones:
    print(c)

print('')

num = int(input("Ingresa 1 número de la lista: \n"))
print("El alumno", nombres[num], "sacó", calificaciones[num], "en", asignaturas[num])