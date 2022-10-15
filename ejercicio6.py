"""
Mariana realizó una lista de invitados para su fiesta.

Luego 1 persona de la lista canceló.
Otras 2 personas se agregaron.

Pero al final la persona que canceló volvió a confirmar.

Utiliza la función copy() para obtener la lista original.
"""

lista_amigos = ['Mario','Carlos','Roberto','Juan','Andrés','Mary','Ernesto','Rubén','Oscar','Sergio']
nueva_lista = lista_amigos.copy()

print("Mi lista de invitados es: \n")
for n in nueva_lista:
    print("·", n)

print('')

cancelo = nueva_lista.pop()
print("Oh no, ha cancelado: ", cancelo)
print('')

def lista():
    for n in range(2):
        nuevo_amigo = input("Pero ahora se han sumado nuevos amigo a la lista de invitados: ")
        nueva_lista.append(nuevo_amigo)
    
lista()

print('')

nueva_lista.append(cancelo)
print("Quiero corregir mi lista ya que" ,cancelo, "ha vuelvo a confirmar su asistecia. \n")

print("Confirmada su asistencia amigos, nos vemos en la fiesta !! \n")
for n in nueva_lista:
    print("·", n)