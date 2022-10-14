"""
Para una boda, necesitan grardar los nombres de 5 invitados.
"Jorge", "Maria", "Juan", "Pedro", "Santiago".

A última hora, Santiago a dicho que no irá por lo que se debe eliminar de la lista.
A última hora Miriam confirmó su asistencia, por lo que se deberá aregar a la lista.
"""

lista_invitados = []

def boda():
    
    for i in range(0, 5):
        invitado = input("Introduce el nombre del invitado: ")
        lista_invitados.append(invitado)

boda()

print('')

print("Mis invitados son: ")
for invitado in lista_invitados:
    print(invitado)

print('')

print("Oh no, me ha cancelado un invitado...")
cancelo = lista_invitados.pop()
print("Ha cancelado ", cancelo)
print("Ha quedado un lugar disponible: ", lista_invitados)

print('')

nuevo_invitado = input("Alguien desea asistir a mi boda?: ")
lista_invitados.append(nuevo_invitado)

print('')

print("Listo, se ha vuelto a completar la lista de invitados: ")
print('')
for invitados_finales in lista_invitados:
    print(invitados_finales)