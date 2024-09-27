class Numero:
    def __init__(self, num):
        self.num = num

    def espar(self):
        return self.num % 2 == 0

while True:
    numero = int(input("\nIngresa un número: "))
    if numero == 0:
        break
    nm = Numero(numero)
    if nm.espar():
        print("\nEl número es par.")
    else:
        print("\nEl número es impar.")

