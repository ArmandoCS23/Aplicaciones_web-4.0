import web
import csv

class ModeloProductos:
    def __init__(self):
        self.productos = []

    def listaProductos(self):
        json_productos = json.dumps(self.productos)
        return json_productos

    def insertarProducto(self, producto):
        self.productos.append(producto)
        return True

    def borrarProducto(self, id_producto):
        for producto in self.productos:
            if producto['id_producto'] == id_producto:
                self.productos.remove(producto)
                return True
        return False

    def detalleProducto(self, id_producto):
        for producto in self.productos:
            if producto['id_producto'] == id_producto:
                return producto
        return None

    def actualizarProducto(self, producto_actualizado):
        for index, producto in enumerate(self.productos):
            if producto['id_producto'] == producto_actualizado['id_producto']:
                self.productos[index] = producto_actualizado
                return True
        return False

render = web.template.render('Views/')

class ListaProductos:
    def GET(self):
        modelo = ModeloProductos()
        productos = modelo.listaProductos()
        return render.lista_productos(productos)

class InsertarProductos:
    def POST(self):
        data = web.input()
        modelo = ModeloProductos()
        producto = {
            'id_producto': int(data.id_producto),
            'nombre': data.nombre,
            'precio': float(data.precio),
            'descripcion': data.descripcion
        }
        exito = modelo.insertarProducto(producto)
        if exito:
            return "Producto insertado exitosamente"
        else:
            return "Error al insertar el producto"

class BorrarProductos:
    def POST(self):
        data = web.input()
        id_producto = int(data.id_producto)
        modelo = ModeloProductos()
        exito = modelo.borrarProducto(id_producto)
        if exito:
            return "Producto borrado exitosamente"
        else:
            return "Error al borrar el producto"

class DetalleProductos:
    def GET(self, id_producto):
        modelo = ModeloProductos()
        producto = modelo.detalleProducto(int(id_producto))
        return render.detalle_productos(producto)

class ActualizarProductos:
    def GET(self, id_producto):
        modelo = ModeloProductos()
        producto = modelo.detalleProducto(int(id_producto))
        return render.actualizar_productos(producto)

    def POST(self):
        data = web.input()
        modelo = ModeloProductos()
        producto_actualizado = {
            'id_producto': int(data.id_producto),
            'nombre': data.nombre,
            'precio': float(data.precio),
            'descripcion': data.descripcion
        }
        exito = modelo.actualizarProducto(producto_actualizado)
        if exito:
            return "Producto actualizado exitosamente"
        else:
            return "Error al actualizar el producto"

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()