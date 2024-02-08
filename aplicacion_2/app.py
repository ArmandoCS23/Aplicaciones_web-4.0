"""Framework web.py"""
import web

# Rutas de los controles
urls = (
    '/', 'mvc.controllers.index.Index'
    '/contactos', 'mvc.controllers.contactos.Contactos'
)

app = web.application(urls, globals())

#Punto de entrada
if__name__=="__main__":
    web.config.debug  = False
    app.run()