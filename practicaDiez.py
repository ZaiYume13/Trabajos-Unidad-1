#Desarrolla un sistema en el cual se inserta un billete o se le indica
# una cantidad a cambiar, el sistema devuelve la cantidad en monedas de $10, $5 y $1
#REGLA GENERAL: no se puede devolver todo de una sola moneda. Tiene que regresar al menos una 
# de cada denominación.

def cambiar_dinero(cantidad):
    monedas_de_diez = 0
    monedas_de_cinco = 0
    monedas_de_uno = 0

    if cantidad >= 10:
        monedas_de_diez = cantidad // 10
        cantidad = cantidad % 10
    if cantidad >= 5:
        monedas_de_cinco = cantidad // 5
        cantidad = cantidad % 5
    if cantidad > 0:
        monedas_de_uno = cantidad
    if monedas_de_diez > 0 and monedas_de_cinco == 0 and monedas_de_uno == 0:
        monedas_de_diez -= 1
        monedas_de_cinco = 1
        monedas_de_uno = (10 - monedas_de_diez * 10) % 5
    elif monedas_de_diez == 0 and monedas_de_cinco > 0 and monedas_de_uno == 0:
        monedas_de_cinco -= 1
        monedas_de_uno = 5

    return 
        "monedas_de_10": monedas_de_diez
        "monedas_de_5": monedas_de_cinco
        "monedas_de_1": monedas_de_uno
   

 uso
cantidad = int(input("Introduce la cantidad a cambiar: "))
resultado = cambiar_dinero(cantidad)
print(f"Monedas de $10: {resultado['monedas_de_10']}")
print(f"Monedas de $5: {resultado['monedas_de_5']}")
print(f"Monedas de $1: {resultado['monedas_de_1']}"))

    
