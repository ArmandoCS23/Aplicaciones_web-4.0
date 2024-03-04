import web
from Mvc.Models.modelo_productos import ModeloProductos 

render = web.template.render('Views/')

class BorrarProductos:
    def POST(self, id_producto):
        modelo = ModeloProductos()
        exito = modelo.borrarProducto(int(id_producto))
        if exito:
            return "Producto borrado exitosamente"
        else:
            return "Error al borrar el producto"

urls = (
    '/borrar/(.*)', 'BorrarProductos'
)
