def leer_texto(mensaje):
    while True:
        texto = input(mensaje).strip()

        if texto == "":
            print("Error: este campo no puede estar vacío.")
        elif any(char.isdigit() for char in texto):
            print("Error: no debe ingresar números en este campo.")
        else:
            return texto


def leer_precio(mensaje):
    while True:
        try:
            precio = float(input(mensaje))

            if precio <= 0:
                print("Error: el precio debe ser mayor que 0.")
            else:
                return precio

        except ValueError:
            print("Error: debe ingresar un número válido.")


def leer_cantidad(mensaje):
    while True:
        try:
            cantidad = int(input(mensaje))

            if cantidad <= 0:
                print("Error: la cantidad debe ser mayor que 0.")
            else:
                return cantidad

        except ValueError:
            print("Error: debe ingresar un número entero válido.")


def leer_porcentaje(mensaje):
    while True:
        try:
            porcentaje = float(input(mensaje))

            if porcentaje < 0 or porcentaje > 100:
                print("Error: el porcentaje debe estar entre 0 y 100.")
            else:
                return porcentaje

        except ValueError:
            print("Error: debe ingresar un porcentaje válido.")


def calcular_subtotal(precio, cantidad):
    subtotal = precio * cantidad
    return subtotal


def calcular_descuento(subtotal, porcentaje):
    descuento = subtotal * porcentaje / 100
    return descuento


def calcular_iva(subtotal, descuento, impuesto):
    base = subtotal - descuento
    iva = base * impuesto / 100
    return iva


def calcular_total(precio, cantidad, porcentaje, impuesto):
    subtotal = calcular_subtotal(precio, cantidad)
    descuento = calcular_descuento(subtotal, porcentaje)
    iva = calcular_iva(subtotal, descuento, impuesto)

    total = subtotal - descuento + iva

    return total, subtotal, descuento, iva


def mostrar_factura(
    cliente,
    producto,
    precio,
    cantidad,
    subtotal,
    porcentaje,
    descuento,
    impuesto,
    iva,
    total
):
    print("\n========================================")
    print("              FACTURA")
    print("========================================")
    print(f"Cliente: {cliente}")
    print(f"Producto: {producto}")
    print(f"Precio unitario: ${precio:.2f}")
    print(f"Cantidad: {cantidad}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Descuento ({porcentaje:.2f}%): ${descuento:.2f}")
    print(f"IVA ({impuesto:.2f}%): ${iva:.2f}")
    print("----------------------------------------")
    print(f"TOTAL A PAGAR: ${total:.2f}")
    print("========================================")


def main():

    print("========================================")
    print("       SISTEMA DE FACTURACIÓN")
    print("========================================")

    # Datos del cliente y producto
    cliente = leer_texto("Ingrese el nombre del cliente: ")
    producto = leer_texto("Ingrese el nombre del producto: ")

    # Datos numéricos
    precio = leer_precio("Ingrese el precio del producto: $")
    cantidad = leer_cantidad("Ingrese la cantidad: ")
    porcentaje = leer_porcentaje("Ingrese el porcentaje de descuento: ")
    impuesto = leer_porcentaje("Ingrese el porcentaje de IVA: ")

    # Cálculos
    total, subtotal, descuento, iva = calcular_total(
        precio,
        cantidad,
        porcentaje,
        impuesto
    )

    # Mostrar factura
    mostrar_factura(
        cliente,
        producto,
        precio,
        cantidad,
        subtotal,
        porcentaje,
        descuento,
        impuesto,
        iva,
        total
    )


main()