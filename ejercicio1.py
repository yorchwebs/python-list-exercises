"""Crea una lista que guarde los nombre de 5 amigos"""

lista_amigos=[]

def amigos():
    
    for x in range(5):
        nuevo_amigo = input("Ingresa el nombre de tu mejor amigo: ")
        lista_amigos.append(nuevo_amigo)

amigos()

print('')

print("Mis 5 mejores amigos son:")
for n in lista_amigos:
    print("·", n)