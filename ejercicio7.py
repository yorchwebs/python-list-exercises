"""
Maria anotó en una lista los nombres de 10 de sus amigos.

El último nombre en anotarse, lo eliminó madiante un pop.

¿Puede Maria recuperar el nombre eliminado?

Realiza un programa que utilice pop() para eliminar el último
valor y después muestra este valor al usuario.
"""

lista_nombres = ['Jorge', 'Oscar', 'Miriam', 'Daniela','Carlos', 'Joselyn','Julio','Camila','Roberto','Mariano']

print("Mi lista de amigos es: \n")
for n in lista_nombres:
    print("·", n)

print('')

print("Uno de mis amigos se molestó y ha dejado de ser mi amigo... \n")
eliminado = lista_nombres.pop()
print("Quien dejó de ser mi amigo es: ", eliminado)

print('')

print("Ahora tengo menos amigos: \n")
for n in lista_nombres:
    print("·", n)