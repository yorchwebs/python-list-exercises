"""
Un profesor necesita guardar las calificaciones de 3 alumnos.
Sus notas: 10, 5, 6.
A última hora necesita agregar sus nombres: "José", "Maria" y "Pablo".
Por último necesita visualizar las calificaciones y los nombres de los estudiantes.
Una impresión podría ser "José sacó 10".
"""

def validar_nombre(message):
    
    while True:
        try:
            data = input("Ingresa " + message)
            return data
        except ValueError:
            print("El dato debe ser texto.")

def validar_nota(message):
    
    while True:
        try:
            data = float(input("Ingresa " + message))
            return data
        except ValueError:
            print("El dato debe ser entero o decimal.")

nombres = []
notas = []

def listas():
    for x  in range(0, 3):
        name = validar_nombre("el nombre del alumno: ")
        nombres.append(name)
        note = validar_nota("su calificación: ")
        notas.append(note)

listas()

print('')

print("Nombre de los alumnos: ")
for name in nombres:
    print(name)

print('')

print("Nombres:")
for nombre in nombres:
    print(nombre)

print('')

print("Calificaciones:")
for nota in notas:
    print(nota)

print('')

num = int(input("Ingresa el número de lista del estudiante: "))

print(nombres[num], "sacó", notas[num])