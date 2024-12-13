from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),  # Página principal
    path('charts/', charts, name='charts'),  # Ruta para la página de gráficos
    path('layout-sidenav-light/', layoutsidenavlight, name='layout-sidenav-light'),  # Ruta para el layout con sidenav light
    path('layout-static/', layoutstatic, name='layout-static'),  # Ruta para el layout estático
    path('tables/', tables, name='tables'),  # Ruta para la página de tablas
    path('accounts/login/', login, name='login'),  # Página de login (requiere autenticación)
    path('accounts/password/', password, name='password'),  # Página de cambio de contraseña
    path('accounts/register/', register, name='register'),  # Página de registro
    path('accounts/clientes/', listar_clientes, name = 'listar_clientes'),
    path('accounts/clientes/editar/<int:cliente_id>/', editar_cliente, name='editar_cliente'),
    path('accounts/clientes/delete/<int:cliente_id>/', delete_cliente, name='delete_cliente'),
    path('accounts/ventas/', obtener_ventas, name = 'obtener_ventas'),
    path('accounts/ventas/<int:venta_id>/', detalle_venta, name = 'detalle_venta'),
    path('accounts/productos/', listar_productos, name = 'listar_productos'),
    path('accounts/productos/<int:producto_id>/', detalle_producto, name = 'detalle_producto'),
    path('accounts/crear/', obtener_nombres_clientes, name = 'obtener_nombres_clientes' ),
    path('accounts/crear-cliente/', crear_cliente, name='crear_cliente'),
]
