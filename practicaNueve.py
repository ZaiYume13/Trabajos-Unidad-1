class Menu:
    def __init__(self):
        self.op = 0

    def mostrar(self):
        print("\n **** M E N Ú **** \n")
        print("1. Opción 1")
        print("2. Opción 2")
        print("3. Opción 3")
        print("4. Opción 4")
        print("5. Salir")

    def elegir(self):
        self.op = int(input("\nElige una opción: "))

    def hacerOp(self):
        while self.op != 5:
            if self.op == 1:
                print("\nSeleccionaste la opción 1\n")
            elif self.op == 2:
                print("\nSeleccionaste la opción 2\n")
            elif self.op == 3:
                print("\nSeleccionaste la opción 3\n")
            elif self.op == 4:
                print("\nSeleccionaste la opción 4\n")
            else:
                print("\nSaliste del programa\n")

            self.mostrar()
            self.elegir()

menu = Menu()
menu.mostrar()
menu.elegir()
menu.hacerOp()



