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

totalsuma = 0

while True:
    num = int(input("\nIngresa un número: "))

    if num == 0:
        print("\nPrograma terminado.")
        break
    totalsuma += num
    suma = SumaDigitos(num)
    print(f"\nLa suma de los dígitos de {num} es {suma.suma_digitos()}")

sumatotal = SumaDigitos(totalsuma).suma_digitos()
print(f"\nLa sumatoria de todos los números ingresados es {totalsuma}")
print(f"La suma de los dígitos de la sumatoria es {sumatotal}")
