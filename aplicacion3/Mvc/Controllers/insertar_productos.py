import web
from Mvc.Models.modelo_productos import ModeloProductos 

render = web.template.render('Views/')

class InsertarProductos:
    def POST(self):
        data = web.input()
        modelo = ModeloProductos()
        producto = {
            'nombre': data.nombre,
            'precio': float(data.precio),
            'descripcion': data.descripcion
        }
        exito = modelo.insertarProducto(producto)
        if exito:
            return "Producto insertado exitosamente"
        else:
            return "Error al insertar el producto"
