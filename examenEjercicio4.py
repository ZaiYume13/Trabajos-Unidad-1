class MayorNumeros:
    def __init__(self):
        self.mayorsumadig = 0
        self.nummayorsuma = 0
        self.cantmenor10 = 0

    def calcularsuma(self, numero):
        suma = 0
        while numero > 0:
            suma += numero % 10
            numero //= 10
        return suma

    def agregarnum(self, numero):
        sumadigitos = self.calcularsuma(numero)
        if sumadigitos > self.mayorsumadig:
            self.mayorsumadig = sumadigitos
            self.nummayorsuma = numero
        if sumadigitos < 10:
            self.cantmenor10 += 1

    def resultado(self):
        print(f"\nEl número con la mayor sumatoria es: {self.nummayorsuma}")
        print(f"\nLa cantidad de números con sumatoria menor que 10 es: {self.cantmenor10}")

mayor = MayorNumeros()

while True:
    numero = int(input("Ingresa un número: "))
    if numero == 0:
        break
    mayor.agregarnum(numero)
mayor.resultado()
