import web
from Mvc.Models.modelo_productos import ModeloProductos 

render = web.template.render('Views/')

class ListaProductos:
    def GET(self):
        modelo = ModeloProductos()  # Crear una instancia de ModeloProductos
        productos = modelo.listaProductos()  # Llamar al método listaProductos de la instancia
        return render.lista_productos(productos)

urls = (
    '/', 'ListaProductos'
)