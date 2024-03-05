import web
from Mvc.Models.modelo_productos import ModeloProductos 

render = web.template.render('Views/')

class DetalleProductos:
    def GET(self, id_producto):
        modelo = ModeloProductos()
        producto = modelo.detalleProducto(int(id_producto))
        return render.detalle_productos(producto)


