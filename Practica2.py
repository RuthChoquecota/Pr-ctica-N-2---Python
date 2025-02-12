ventas=[
    {
        "fecha":"12-01-2023",
        "producto":"Producto_A",
        "cantidad":50,
        "precio":45.00,
        "promocion":True
    },
    {
        "fecha":"11-01-2023",
        "producto":"Producto_AX",
        "cantidad":160,
        "precio":12.00,
        "promocion":False
    },
    {
        "fecha":"10-01-2023",
        "producto":"Producto_D",
        "cantidad":20,
        "precio":15.00,
        "promocion":False
    },
    {
        "fecha":"11-01-2023",
        "producto":"Producto_C",
        "cantidad":10,
        "precio":140.00,
        "promocion":False
    },
    {
        "fecha":"11-01-2023",
        "producto":"Producto_D",
        "cantidad":1200,
        "precio":1.00,
        "promocion":True
    }
]

def mostrar_listado_ventas():
    print("Listado de Ventas:")
    for venta in ventas:
        print(f"Fecha: {venta['fecha']}, Producto: {venta['producto']}, Cantidad: {venta['cantidad']}, Precio: {venta['precio']}, Promoción: {venta['promocion']}")

def anadir_producto():
    fecha = input("Ingrese la fecha (dd-mm-yyyy): ")
    producto = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad: "))
    precio = float(input("Ingrese el precio: "))
    promocion = input("¿Está en promoción? (True/False): ").strip().lower() == 'true'
    nueva_venta = {
        "fecha": fecha,
        "producto": producto,
        "cantidad": cantidad,
        "precio": precio,
        "promocion": promocion
    }
    ventas.append(nueva_venta)
    print("Producto añadido correctamente.")

def calcular_suma_total():
    suma_total = sum(venta['cantidad'] * venta['precio'] for venta in ventas)
    print(f"La suma total de las ventas es: {suma_total:.2f}")

def calcular_promedio_ventas():
    total_ventas = len(ventas)
    if total_ventas > 0:
        promedio = sum(venta['cantidad'] * venta['precio'] for venta in ventas) / total_ventas
        print(f"El promedio de las ventas es: {promedio:.2f}")
    else:
        print("No hay ventas registradas para calcular el promedio.")

def producto_mas_vendido():
    if ventas:
        producto_max = max(ventas, key=lambda x: x['cantidad'])
        print(f"El producto más vendido es: {producto_max['producto']} con {producto_max['cantidad']} unidades.")
    else:
        print("No hay ventas registradas.")

def mostrar_listado_productos():
    productos = {venta['producto'] for venta in ventas}
    print("Listado de Productos:")
    for producto in productos:
        print(producto)

def menu():
    while True:
        print("\nMenú de Opciones:")
        print("2. Mostrar el listado de ventas")
        print("3. Añadir un producto")
        print("4. Calcular la suma total de las ventas")
        print("5. Calcular el promedio de ventas")
        print("6. Mostrar el producto más vendido")
        print("7. Mostrar el listado de productos")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "2":
            mostrar_listado_ventas()
        elif opcion == "3":
            anadir_producto()
        elif opcion == "4":
            calcular_suma_total()
        elif opcion == "5":
            calcular_promedio_ventas()
        elif opcion == "6":
            producto_mas_vendido()
        elif opcion == "7":
            mostrar_listado_productos()
            break
        else:
            print("Opción no válida. Intente nuevamente.")

menu()
