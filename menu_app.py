def agregar_compra(monto,compras):
    compras.append(monto)
    print("La compra se ha agregado correctamente.")

def mostrar_compras(compras):
    if len(compras) > 0:
        for indice,compra in compras:
            print("compra N° ",indice + 1," Monto: ",compra)
    else:
        print("No existen compras registradas")

def mostrar_total(compras,total_gastado):
    for compra in compras:
        total_gastado += compra

    total_gastado = format(round(total_gastado))
    print("$ " +total_gastado)

def main():
    compras = []
    total_gastado = 0
    monto = 0
    while True:
        opcion = int(input("Ingrese una opcion del menu"))
        if opcion == 1:
            agregar_compra(monto,compras)
        elif opcion == 2:
            mostrar_compras(compras)
        elif opcion == 3:
            mostrar_total(compras,total_gastado)
        elif opcion == 4:
            exit()
        else:
            print("Opcion inválida")