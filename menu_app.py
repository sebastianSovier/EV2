def agregar_compra(monto,compras):
    compras.append(monto)
    print("La compra se ha agregado correctamente.")

def mostrar_compras(compras):
    if len(compras) > 0:
        contador = 1
        for compra in compras:
            print("compra N ",contador ," Monto: ",compra)
            contador +=1
    else:
        print("No existen compras registradas")

def mostrar_total(total_gastado):
    print("$ " +format(int(round(total_gastado)),',').replace(",","."))

def main():
    compras = []
    total_gastado = 0
    while True:
        opcion = int(input("Ingrese una opcion del menu"))
        if opcion == 1:
            monto = int(input("Ingrese monto de la compra"))
            agregar_compra(monto,compras)
        elif opcion == 2:
            mostrar_compras(compras)
        elif opcion == 3:
            total_gastado = sum(compras)
            mostrar_total(total_gastado)
        elif opcion == 4:
            exit()
        else:
            print("Opcion invalida")

if __name__ == "__main__":
    main()