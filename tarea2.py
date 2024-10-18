productos = []

def añadir_producto():
    nombre = input("Ingrese el nombre del producto: ")
    while True:
        try:
            precio = float(input("Ingrese el precio del producto: "))
            cantidad = int(input("Ingrese la cantidad disponible: "))
            break
        except ValueError:
            print("Por favor, ingrese valores numéricos válidos para precio y cantidad.")
    
    producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
    productos.append(producto)
    print(f"Producto '{nombre}' añadido exitosamente.")

def ver_productos():
    if not productos:
        print("No hay productos en el inventario.")
    else:
        print("\nLista de Productos:")
        for producto in productos:
            print(f"Nombre: {producto['nombre']}, Precio: ₲{int(producto['precio']):,}, Cantidad: {producto['cantidad']}")

def actualizar_producto():
    nombre = input("Ingrese el nombre del producto a actualizar: ")
    for producto in productos:
        if producto['nombre'].lower() == nombre.lower():
            print(f"Producto encontrado: {producto['nombre']}, Precio: ₲ {int(producto['precio']):,}, Cantidad: {producto['cantidad']}")
            campo = input("¿Qué desea actualizar? (nombre/precio/cantidad): ").lower()
            if campo in ['nombre', 'precio', 'cantidad']:
                if campo == 'nombre':
                    nuevo_valor = input("Ingrese el nuevo nombre: ")
                elif campo == 'precio':
                    while True:
                        try:
                            nuevo_valor = float(input("Ingrese el nuevo precio: "))
                            break
                        except ValueError:
                            print("Por favor, ingrese un valor numérico válido.")
                else:  
                    while True:
                        try:
                            nuevo_valor = int(input("Ingrese la nueva cantidad: "))
                            break
                        except ValueError:
                            print("Por favor, ingrese un valor entero válido.")
                
                producto[campo] = nuevo_valor
                print(f"Producto actualizado exitosamente.")
                return
            else:
                print("Campo no válido.")
                return
    print("Producto no encontrado.")

def eliminar_producto():
    nombre = input("Ingrese el nombre del producto a eliminar: ")
    for producto in productos:
        if producto['nombre'].lower() == nombre.lower():
            productos.remove(producto)
            print(f"Producto '{nombre}' eliminado exitosamente.")
            return
    print("Producto no encontrado.")

def guardar_datos():
    try:
        with open("productos.txt", "w") as archivo:
            for producto in productos:
                archivo.write(f"{producto['nombre']},{int(producto['precio'])},{producto['cantidad']}\n")
        print("Datos guardados exitosamente.")
    except IOError:
        print("Error al guardar los datos.")

def cargar_datos():
    try:
        with open("productos.txt", "r") as archivo:
            for linea in archivo:
                nombre, precio, cantidad = linea.strip().split(",")
                productos.append({"nombre": nombre, "precio": int(float(precio)), "cantidad": int(cantidad)})
        print("Datos cargados exitosamente.")
    except FileNotFoundError:
        print("No se encontró archivo de datos")
    except IOError:
        print("Error al cargar los datos.")

def menu():
    cargar_datos()
    while True:
        print("\n--- Menú de Gestión de Productos ---")
        print("1: Añadir producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos y salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            añadir_producto()
        elif opcion == '2':
            ver_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            guardar_datos()
            print("Bye bye")
            break
        else:
            print("Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    menu()