class Alumno:
	def __init__(self,nombre):
		self.nom = nombre
	def Saludar (self):
		"""Imprime un saludo en la pantalla"""
		print(f" \n ¡Hola,{self.nom}!")

cont = True

while cont:
    n = input("\nEscribe tu nombre: ")
    x = Alumno(n)
    x.Saludar()
    
    resp = input("\n¿Deseas continuar? (si/no): ")
    if resp != 'si':
        cont = False
