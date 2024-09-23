class tablasDeMultiplicar:
    def __init__(self, num):
        self.num = num
cont= True 
while cont:
    def generar_tabla(self):
        print(f"Tabla de multiplicar del {self.num}:")
        for i in range(1, 11):
            print(f"{self.num} x {i} = {self.num * i}")




	num = int(input("Escribe un número para la tabla de multiplicar: "))
	tabla = tablasDeMultiplicar(num)
	tabla.generar_tabla()
	
	resp = input("\n¿Deseas continuar? (si/no): ")
    if resp != 'si':
		cont = False
