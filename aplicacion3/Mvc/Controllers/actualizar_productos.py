import web
from Mvc.Models.modelo_productos import ModeloProductos 
 
render = web.template.render('Views/')

class ActualizarProductos:
    def GET(self, id_producto):
        modelo = ModeloProductos()
        producto = modelo.detalleProducto(id_producto)
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