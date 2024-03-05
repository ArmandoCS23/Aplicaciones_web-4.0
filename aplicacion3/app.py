import web

urls = (
    '/', 'Mvc.Controllers.lista_productos.ListaProductos',
    '/insertar', 'Mvc.Controllers.insertar_productos.InsertarProductos',
    '/borrar', 'Mvc.Controllers.borrar_productos.BorrarProductos',
    '/detalle/(.*)', 'Mvc.Controllers.detalle_productos.DetalleProductos',
    '/actualizar/(.*)', 'Mvc.Controllers.actualizar_productos.ActualizarProductos',
)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()