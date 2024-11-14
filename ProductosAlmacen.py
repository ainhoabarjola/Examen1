productos_almacen = {
    # Diccionario que representa el inventario del almacén, donde cada clave es una estantería
    # y su valor es una lista de productos (cada producto es un diccionario con nombre, cantidad y precio).
    "Estantería A": [{"nombre": "Chocolate Amargo", "cantidad": 20, "precio": 2.5},
                     {"nombre": "Mermelada de Fresa", "cantidad": 15, "precio": 3.0}],
    "Estantería B": [{"nombre": "Aceitunas Verdes", "cantidad": 50, "precio": 1.5},
                     {"nombre": "Aceite de Oliva Extra", "cantidad": 10, "precio": 6.0}],
    "Estantería C": [{"nombre": "Café Molido", "cantidad": 25, "precio": 5.0},
                     {"nombre": "Té Verde", "cantidad": 40, "precio": 2.0}],
    "Estantería D": [{"nombre": "Pasta Integral", "cantidad": 30, "precio": 1.8},
                     {"nombre": "Arroz Basmati", "cantidad": 20, "precio": 1.7}] }

# Función para agregar un nuevo producto a una estantería
def agregar_producto(nombre, cantidad, precio, estanteria):  # Comprobar si la estantería existe
    if estanteria in productos_almacen: # Verificar si el producto ya existe en la estantería
        for producto in productos_almacen[estanteria]: # Recorrer los productos de la estantería
            if producto['nombre'].lower() == nombre.lower():  # Comprobar si el producto ya existe
                producto['cantidad'] += cantidad # Actualizar la cantidad si el producto existe
                print(f"Cantidad actualizada del producto {nombre} en {estanteria}.")
                return
        # Si no existe, agregarlo como nuevo producto
        productos_almacen[estanteria].append({"nombre": nombre, "cantidad": cantidad, "precio": precio})
        print(f"Producto {nombre} agregado correctamente a {estanteria}.")
    else:
        print("Error: La estantería especificada no existe.")

# Función para retirar una cantidad de un producto específico
def retirar_producto(nombre, cantidad_retirar): # Recorrer todas las estanterías
    for estanteria, productos in productos_almacen.items():
        for producto in productos:
            if producto['nombre'].lower() == nombre.lower(): # Verificar si el producto existe
                if producto['cantidad'] >= cantidad_retirar: # Comprobar si hay suficiente cantidad
                    producto['cantidad'] -= cantidad_retirar # Reducir la cantidad
                    print(f"Producto {nombre} retirado correctamente. Cantidad restante: {producto['cantidad']}.")
                    # Si la cantidad llega a 0, opcionalmente podrías eliminarlo de la lista
                    if producto['cantidad'] == 0:
                        productos.remove(producto)
                        print(f"Producto {nombre} eliminado de {estanteria}.")
                    return
                else:
                    print(f"Error: No hay suficiente cantidad de {nombre} para retirar {cantidad_retirar} unidades.")
                    return
    print(f"Error: Producto {nombre} no encontrado en el almacén.")

# Función para verificar si un producto está disponible en el almacén
def verificar_disponibilidad(nombre):
    encontrado = False
    for estanteria, productos in productos_almacen.items(): # Recorrer todas las estanterías
        for producto in productos:
            if producto['nombre'].lower() == nombre.lower(): # Comprobar si el producto está en la estantería
                print(f"Producto {nombre} encontrado en {estanteria} con {producto['cantidad']} unidades disponibles.")
                encontrado = True
    if not encontrado:
        print(f"Producto {nombre} no se encuentra en el almacén.")


# Función para mostrar el estado actual del almacén y su valor total
def estado_almacen():
    total_valor = 0
    for estanteria, productos in productos_almacen.items(): # Recorrer cada estantería
        print(f"\nEstado de {estanteria}:")
        for producto in productos:
            valor_producto = producto['cantidad'] * producto['precio'] # Calcular el valor total de cada producto
            total_valor += valor_producto # Sumar al valor total del almacén
            print(f"- {producto['nombre']}: {producto['cantidad']} unidades, valor total: ${valor_producto:.2f}")
    print(f"\nValor total de todos los productos en el almacén: ${total_valor:.2f}")

# Función para transferir productos de una estantería a otra
def transferir_producto(nombre, cantidad, estanteria_origen, estanteria_destino):
    if estanteria_origen not in productos_almacen or estanteria_destino not in productos_almacen:
        print("Error: Una o ambas estanterías especificadas no existen.")
        return

    for producto in productos_almacen[estanteria_origen]: # Buscar el producto en la estantería de origen
        if producto['nombre'].lower() == nombre.lower():
            if producto['cantidad'] >= cantidad: # Comprobar si hay suficiente cantidad para transferir
                producto['cantidad'] -= cantidad # Reducir la cantidad en la estantería de origen
                if producto['cantidad'] == 0:
                    productos_almacen[estanteria_origen].remove(producto)
                    print(f"Producto {nombre} agotado y eliminado de {estanteria_origen}.")
                # Transferir el producto a la estantería de destino
                for prod_destino in productos_almacen[estanteria_destino]:
                    if prod_destino['nombre'].lower() == nombre.lower():
                        prod_destino['cantidad'] += cantidad
                        print(f"{cantidad} unidades de {nombre} transferidas de {estanteria_origen} a {estanteria_destino}.")
                        return
                # Agregar el producto como nuevo en la estantería de destino si no existe
                productos_almacen[estanteria_destino].append({"nombre": nombre, "cantidad": cantidad, "precio": producto['precio']})
                print(f"{cantidad} unidades de {nombre} transferidas de {estanteria_origen} a {estanteria_destino} como nuevo producto.")
                return
            else:
                print(f"Error: No hay suficiente cantidad de {nombre} en {estanteria_origen} para transferir.")
                return
    print(f"Error: Producto {nombre} no encontrado en {estanteria_origen}.")

# Función para mostrar información optimizada del inventario
def optimizar_inventario():
    estanteria_mayor_valor = ""
    estanteria_menor_productos = ""
    mayor_valor = 0
    menor_cantidad_productos = float('inf')

    # Recorrer todas las estanterías y calcular el valor total y la cantidad de productos
    for estanteria, productos in productos_almacen.items():
        valor_estanteria = sum(p['cantidad'] * p['precio'] for p in productos)
        cantidad_productos = sum(p['cantidad'] for p in productos)

        if valor_estanteria > mayor_valor:
            mayor_valor = valor_estanteria
            estanteria_mayor_valor = estanteria

        if cantidad_productos < menor_cantidad_productos:
            menor_cantidad_productos = cantidad_productos
            estanteria_menor_productos = estanteria

    # Imprimir los resultados de la optimización
    print(f"La estantería con mayor valor acumulado es {estanteria_mayor_valor} con un valor total de ${mayor_valor:.2f}.")
    print(f"La estantería con menos productos es {estanteria_menor_productos} con un total de {menor_cantidad_productos} unidades.")
