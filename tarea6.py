# Clase base Prenda
class Prenda:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def mostrar_info(self):
        return f"Nombre: {self.nombre}, Precio: {self.precio}, Cantidad: {self.cantidad}"

# Clase RopaHombre que hereda de Prenda
class RopaHombre(Prenda):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad)  # Llamamos al constructor de la clase base
        self.talla = talla

    def mostrar_info(self):
        return f"{super().mostrar_info()}, Talla: {self.talla} (Hombre)"

# Clase RopaMujer que hereda de Prenda
class RopaMujer(Prenda):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad)  # Llamamos al constructor de la clase base
        self.talla = talla

    def mostrar_info(self):
        return f"{super().mostrar_info()}, Talla: {self.talla} (Mujer)"

# Clase Inventario que gestiona las prendas
class Inventario:
    def __init__(self):
        self.prendas = []

    def agregar_prenda(self, prenda):
        self.prendas.append(prenda)

    def mostrar_inventario(self):
        print("\nInventario disponible:")
        for idx, prenda in enumerate(self.prendas, 1):
            print(f"{idx}. {prenda.mostrar_info()}")

    def procesar_compra(self, nombre_prenda, cantidad_compra):
        for prenda in self.prendas:
            if prenda.nombre == nombre_prenda and prenda.cantidad >= cantidad_compra:
                prenda.cantidad -= cantidad_compra
                print(f"\nCompra procesada: {cantidad_compra} {prenda.nombre}")
                print(f"Cantidad restante: {prenda.cantidad}")
                return True
        print("\nNo hay suficiente stock o la prenda no existe.")
        return False

# Función principal que interactúa con el usuario
def realizar_compra(inventario):
    while True:
        inventario.mostrar_inventario()
        
        try:
            seleccion = int(input("\nSeleccione el número de la prenda que desea comprar (0 para salir): "))
            
            if seleccion == 0:
                print("¡Gracias por su compra!")
                break
            
            prenda_seleccionada = inventario.prendas[seleccion - 1]
            
            cantidad = int(input(f"¿Cuántas unidades de {prenda_seleccionada.nombre} desea comprar?: "))
            
            if inventario.procesar_compra(prenda_seleccionada.nombre, cantidad):
                print(f"Compra exitosa de {cantidad} unidades de {prenda_seleccionada.nombre}.")
                
        except (ValueError, IndexError):
            print("Selección no válida. Intente de nuevo.")

# Ejemplo de uso del sistema de compras

# Crear instancias de ropa para hombre y mujer
camisa_hombre = RopaHombre("Camisa de Hombre", 25.00, 50, "M")
falda_mujer = RopaMujer("Falda de Mujer", 28.00, 15, "S")
pantalon_hombre = RopaHombre("Pantalón de Hombre", 30.00, 30, "L")
blusa_mujer = RopaMujer("Blusa de Mujer", 22.00, 40, "M")

# Crear inventario y agregar las prendas
inventario = Inventario()
inventario.agregar_prenda(camisa_hombre)
inventario.agregar_prenda(falda_mujer)
inventario.agregar_prenda(pantalon_hombre)
inventario.agregar_prenda(blusa_mujer)

# Iniciar el proceso de compra
realizar_compra(inventario)