import web
from Mvc.Controllers import lista_productos, insertar_productos, borrar_productos, detalle_productos, actualizar_productos

urls = (
    '/', 'lista_productos.ListaProductos',
    '/insertar', 'insertar_productos.InsertarProductos',
    '/borrar', 'borrar_productos.BorrarProductos',
    '/detalle/(.*)', 'detalle_productos.DetalleProductos',
    '/actualizar/(.*)', 'actualizar_productos.ActualizarProductos',
)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
