# ============================================
# SISTEMA DE FACTURACIÓN
# PROGRAMACIÓN ESTRUCTURADA
# SIN UTILIZAR LISTAS
# ============================================


# --------------------------------------------
# FUNCIÓN PARA LEER EL NOMBRE DEL CLIENTE
# --------------------------------------------
def leer_cliente():

    while True:
        nombre = input("Ingrese el nombre del cliente: ").strip()

        if nombre == "":
            print("Error: el nombre no puede estar vacío.")

        elif nombre.replace(" ", "").isdigit():
            print("Error: el nombre no puede ser solamente un número.")

        else:
            return nombre


# --------------------------------------------
# FUNCIÓN PARA LEER CANTIDAD DE PRODUCTOS
# --------------------------------------------
def leer_cantidad_productos():

    while True:
        try:
            cantidad = int(
                input("Ingrese la cantidad de productos: ")
            )

            if cantidad <= 0:
                print("Error: debe ingresar una cantidad mayor que 0.")

            else:
                return cantidad

        except ValueError:
            print("Error: debe ingresar un número entero.")


# --------------------------------------------
# FUNCIÓN PARA CALCULAR SUBTOTAL
# --------------------------------------------
def calcular_subtotal(precio, cantidad):

    return precio * cantidad


# --------------------------------------------
# FUNCIÓN PARA CALCULAR DESCUENTO
# --------------------------------------------
def calcular_descuento(subtotal, porcentaje):

    return subtotal * porcentaje / 100


# --------------------------------------------
# FUNCIÓN PARA CALCULAR LOS PRODUCTOS
# --------------------------------------------
def calcular_total_productos(cantidad_productos):

    contador = 1
    suma_subtotales = 0
    subtotal_mayor = 0

    while contador <= cantidad_productos:

        print("\n------------------------------------------")
        print("PRODUCTO", contador)
        print("------------------------------------------")

        # ------------------------------------
        # VALIDAR NOMBRE DEL PRODUCTO
        # ------------------------------------
        while True:

            nombre_producto = input(
                "Ingrese el nombre del producto: "
            ).strip()

            if nombre_producto == "":
                print(
                    "Error: el nombre del producto "
                    "no puede estar vacío."
                )

            elif nombre_producto.isdigit():
                print(
                    "Error: el nombre del producto "
                    "no puede ser solamente un número."
                )

            else:
                break

        # ------------------------------------
        # VALIDAR PRECIO
        # ------------------------------------
        while True:

            try:

                precio = float(
                    input("Ingrese el precio del producto: ")
                )

                if precio <= 0:
                    print(
                        "Error: el precio debe ser mayor que 0."
                    )

                else:
                    break

            except ValueError:

                print(
                    "Error: ingrese un precio válido."
                )

        # ------------------------------------
        # VALIDAR CANTIDAD
        # ------------------------------------
        while True:

            try:

                cantidad = int(
                    input("Ingrese la cantidad: ")
                )

                if cantidad <= 0:
                    print(
                        "Error: la cantidad debe ser mayor que 0."
                    )

                else:
                    break

            except ValueError:

                print(
                    "Error: ingrese una cantidad entera válida."
                )

        # ------------------------------------
        # CALCULAR SUBTOTAL
        # ------------------------------------
        subtotal = calcular_subtotal(
            precio,
            cantidad
        )

        print(
            "Subtotal del producto:",
            round(subtotal, 2)
        )

        # ------------------------------------
        # ACUMULAR SUBTOTALES
        # ------------------------------------
        suma_subtotales = (
            suma_subtotales + subtotal
        )

        # ------------------------------------
        # DETERMINAR MAYOR SUBTOTAL
        # ------------------------------------
        if contador == 1:

            subtotal_mayor = subtotal

        elif subtotal > subtotal_mayor:

            subtotal_mayor = subtotal

        contador = contador + 1

    return suma_subtotales, subtotal_mayor


# --------------------------------------------
# FUNCIÓN PARA OBTENER EL MAYOR SUBTOTAL
# --------------------------------------------
def calcular_subtotal_mayor(subtotal_mayor):

    return subtotal_mayor


# --------------------------------------------
# FUNCIÓN PARA CALCULAR TOTAL
# --------------------------------------------
def calcular_total(
    subtotal,
    descuento,
    iva
):

    subtotal_descuento = (
        subtotal - descuento
    )

    impuesto = (
        subtotal_descuento * iva / 100
    )

    total = (
        subtotal_descuento + impuesto
    )

    return impuesto, total


# --------------------------------------------
# FUNCIÓN PARA MOSTRAR FACTURA
# --------------------------------------------
def mostrar_factura(
    nombre,
    subtotal,
    porcentaje_descuento,
    descuento,
    iva,
    impuesto,
    total,
    subtotal_mayor
):

    print("\n")
    print("==========================================")
    print("              FACTURA")
    print("==========================================")

    print("Cliente:", nombre)

    print("------------------------------------------")

    print(
        "Subtotal:",
        round(subtotal, 2)
    )

    print(
        "Descuento:",
        porcentaje_descuento,
        "%"
    )

    print(
        "Valor del descuento:",
        round(descuento, 2)
    )

    print(
        "IVA:",
        iva,
        "%"
    )

    print(
        "Valor del IVA:",
        round(impuesto, 2)
    )

    print("------------------------------------------")

    print(
        "Mayor subtotal:",
        round(subtotal_mayor, 2)
    )

    print("------------------------------------------")

    print(
        "TOTAL A PAGAR:",
        round(total, 2)
    )

    print("==========================================")


# ============================================
# FUNCIÓN PRINCIPAL
# ============================================
def main():

    print("==========================================")
    print("       SISTEMA DE FACTURACIÓN")
    print("==========================================")

    # ----------------------------------------
    # 1. LEER CLIENTE
    # ----------------------------------------
    nombre = leer_cliente()

    # ----------------------------------------
    # 2. LEER CANTIDAD DE PRODUCTOS
    # ----------------------------------------
    cantidad_productos = (
        leer_cantidad_productos()
    )

    # ----------------------------------------
    # 3. PROCESAR PRODUCTOS
    # ----------------------------------------
    subtotal, subtotal_mayor = (
        calcular_total_productos(
            cantidad_productos
        )
    )

    # ----------------------------------------
    # 4. OBTENER MAYOR SUBTOTAL
    # ----------------------------------------
    subtotal_mayor = (
        calcular_subtotal_mayor(
            subtotal_mayor
        )
    )

    # ----------------------------------------
    # 5. VALIDAR DESCUENTO
    # ----------------------------------------
    while True:

        try:

            porcentaje_descuento = float(
                input(
                    "\nIngrese porcentaje de descuento: "
                )
            )

            if porcentaje_descuento < 0:

                print(
                    "Error: el descuento no "
                    "puede ser negativo."
                )

            elif porcentaje_descuento > 100:

                print(
                    "Error: el descuento no "
                    "puede ser mayor que 100%."
                )

            else:

                break

        except ValueError:

            print(
                "Error: ingrese un porcentaje válido."
            )

    # ----------------------------------------
    # 6. CALCULAR DESCUENTO
    # ----------------------------------------
    descuento = calcular_descuento(
        subtotal,
        porcentaje_descuento
    )

    # ----------------------------------------
    # 7. VALIDAR IVA
    # ----------------------------------------
    while True:

        try:

            iva = float(
                input("\nIngrese porcentaje de IVA: ")
            )

            if iva < 0:

                print(
                    "Error: el IVA no puede ser negativo."
                )

            elif iva > 100:

                print(
                    "Error: el IVA no puede ser mayor que 100%."
                )

            else:

                break

        except ValueError:

            print(
                "Error: ingrese un porcentaje válido."
            )

    # ----------------------------------------
    # 8. CALCULAR IMPUESTO Y TOTAL
    # ----------------------------------------
    impuesto, total = calcular_total(
        subtotal,
        descuento,
        iva
    )

    # ----------------------------------------
    # 9. MOSTRAR FACTURA
    # ----------------------------------------
    mostrar_factura(
        nombre,
        subtotal,
        porcentaje_descuento,
        descuento,
        iva,
        impuesto,
        total,
        subtotal_mayor
    )


# ============================================
# EJECUTAR PROGRAMA
# ============================================
main()
