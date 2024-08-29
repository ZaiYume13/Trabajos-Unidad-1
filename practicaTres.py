class Nombre:		#Inicia clase nombre 
	def __init__(self,nom):
		self.h = nom
		
s = Nombre ("Ingresa tu nombre: ")    #Imprime y pide tu nombre
input(s.h)
