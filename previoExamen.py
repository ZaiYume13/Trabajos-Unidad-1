#El sistema para cosecha de manzanas a cada trabajador se le paga por caja de 
# manzanas cosechadas las primeras 10 cajas se le pagan a $50 cada caja, mas de 50
# y menos de 80 cajas se le pagan 50% más, más de 80 se le paga el doble de su  total de pago
#Se le descuenta el 5% para cada de ahorro. Generar un sistema que pida el nombre del 
# trabajador y la cantidad de cajas cosechadas asi como el descuento que se hace por su pago.  

class Trabajador:
    def __init__(self, nombre, cajas):
        self.nombre = nombre
        self.cajas = cajas
        self.pago_bruto, self.cajas_50, self.cajas_75 = self.calcular()
        self.descuento = self.pago_bruto * 0.05
        self.pago_neto = self.pago_bruto - self.descuento

    def calcular(self):
        cajas_50 = 0
        cajas_75 = 0
        if self.cajas <= 10:
            pago = self.cajas * 50
            cajas_50 = self.cajas
        elif 10 < self.cajas <= 50:
            pago = 10 * 50 + (self.cajas - 10) * 75
            cajas_50 = 10
            cajas_75 = self.cajas - 10
        elif 50 < self.cajas <= 80:
            pago = 10 * 50 + 40 * 75 + (self.cajas - 50) * 75 * 1.5
            cajas_50 = 10
            cajas_75 = self.cajas - 10
        else:
            pago = self.cajas * 100
            cajas_50 = 10
            cajas_75 = 40 + (self.cajas - 50)
            
        return pago, cajas_50, cajas_75

    def imprimir(self):
        print(f"\nEl trabajador: {self.nombre}")
        print(f"\nCajas cosechadas: {self.cajas}")
        print(f"\nPago bruto: ${self.pago_bruto:.2f}")
        print(f"\nDescuento (5%): ${self.descuento:.2f}")
        print(f"\nPago neto: ${self.pago_neto:.2f}")
        print(f"\nCajas pagadas a $50: {self.cajas_50}")
        print(f"\nCajas pagadas a $75: {self.cajas_75}\n")

nombre = input("\nIngrese el nombre del trabajador: ")
cajas = int(input("Ingrese la cantidad de cajas cosechadas: "))
trabajador = Trabajador(nombre, cajas)
trabajador.imprimir()


