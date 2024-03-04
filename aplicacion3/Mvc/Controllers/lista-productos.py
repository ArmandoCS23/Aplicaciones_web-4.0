import web
from Models.modelo_productos import ModeloProductos

render = web.template.render('Views/')

class ListaProductos:
    def GET(self):
        modelo = ModeloProductos()
        productos = modelo.listaProductos()
        return render.lista_productos(productos)

urls = (
    '/', 'ListaProductos'
)
