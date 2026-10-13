# path: función para definir una ruta individual
from django.urls import path
# views: el archivo que acabás de escribir, en la misma carpeta
from . import views

# urlpatterns: lista de rutas que esta app entiende
urlpatterns = [
    # '': la URL vacía (la raíz de esta app) · views.inicio: la función que la atiende
    # name='inicio': un alias interno para referirse a esta ruta sin escribir la URL a mano
    path('', views.inicio, name='inicio'),
    # nueva ruta 'servicios/' → función views.servicios → alias 'servicios'
    path('catalogo/', views.servicios, name='servicios'),


    ### SE AGRAGRON ESTOS
    path('servicios/', views.servicios, name='servicios'),
    # /servicios/nuevo/: formulario en blanco para crear un registro
    path('servicios/nuevo/', views.crear_servicio, name='crear_servicio'),
    # /servicios/<int:pk>/editar/: <int:pk> captura el id de la URL y lo pasa como argumento a la vista
    path('servicios/<int:pk>/editar/', views.editar_servicio, name='editar_servicio'),
    # /servicios/<int:pk>/eliminar/: mismo patrón, para la pantalla de confirmación de borrado
    path('servicios/<int:pk>/eliminar/', views.eliminar_servicio, name='eliminar_servicio'),
]