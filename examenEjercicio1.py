class SumaDigitos:
    def __init__(self, num):
        self.num = num

    def suma_digitos(self):
        suma = 0
        num = self.num
        while num != 0:
            suma += num % 10
            num //= 10
        return suma

while True:
    num = int(input("\nIngresa un número: "))
    if num == 0:
        print("\nPrograma terminado.")
        break
    suma = SumaDigitos(num)
    print(f"\nLa suma de los dígitos de {num} es {suma.suma_digitos()}")

