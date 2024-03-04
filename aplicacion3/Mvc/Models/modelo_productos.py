import json

class ModeloProductos:
    def __init__(self):
        # Aquí podrías inicializar alguna estructura de datos para almacenar los productos, por ejemplo, una lista vacía.
        self.productos = []

    def listaProductos(self):
        # Código para consultar todos los productos
        # Generar un JSON con los productos
        json_productos = json.dumps([producto.__dict__ for producto in self.productos])
        return json_productos

    def insertarProducto(self, producto):
        # Código para insertar un producto
        # Agregar el producto a la lista de productos
        self.productos.append(producto)
        return True  # Si se inserta correctamente, podrías devolver True

    def borrarProducto(self, id_producto):
        # Código para borrar un producto por su ID
        # Buscar el producto por su ID y borrarlo
        for producto in self.productos:
            if producto.id_producto == id_producto:
                self.productos.remove(producto)
                return True  # Si se borra correctamente, podrías devolver True
        return False  # Si no se encuentra el producto, podrías devolver False

    def detalleProducto(self, id_producto):
        # Código para obtener el detalle de un producto por su ID
        # Buscar el producto por su ID y devolver su detalle
        for producto in self.productos:
            if producto.id_producto == id_producto:
                return producto.__dict__
        return None  # Si no se encuentra el producto, podrías devolver None

    def actualizarProducto(self, producto_actualizado):
        # Código para actualizar un producto
        # Buscar el producto por su ID y actualizar sus atributos
        for index, producto in enumerate(self.productos):
            if producto.id_producto == producto_actualizado.id_producto:
                self.productos[index] = producto_actualizado
                return True  # Si se actualiza correctamente, podrías devolver True
        return False  # Si no se encuentra el producto, podrías devolver False
