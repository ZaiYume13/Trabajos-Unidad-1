class Datos:
	def __init__(self):
		self.n = input("\nEscribe tu nombre: ")
		self.c1 = int(input("\nEscribe la 1° calificación: "))
		self.c2 = int(input("Escribe la 2° calificación: "))
		self.c3 = int(input("Escribe la 3° calificación: "))
		self.p = 0
	
class Promedio(Datos):	
	def prom(self):
		if self.c1 < 70 and self.c2 < 70 and self.c3 < 70:
			self.p = 0
		else:
			self.p = (self.c1 + self.c2 + self.c3)/3
			self.p = round(self.p,3)

class Comparacion(Promedio):
	def comparacion(self):
		if self.c1 < 70 or self.c2 < 70 or self.c3 < 70:
			return " REPROBADO"
		else:
			return " APROBADO"

class Imprimir(Comparacion):
	def imprimir(self):
		self.p()
		e = self.comparacion
		print(f"\n{self.n} con calificaciones: {self.c1}, {self.c2}, {self.c3} Tuvo un promedio de: {self.p} y está: {e}")

x = Imprimir()
x.imprimir()
