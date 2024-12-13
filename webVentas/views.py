from pyexpat.errors import messages
from django.shortcuts import get_object_or_404, render, redirect
import requests
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib import messages

def index(request):
    return render(request, 'core/index.html')

@login_required
def login(request):
    return render(request, 'registration/login.html')

def password(request):
    return render(request, 'registration/password.html')
def register(request):
    return render(request, 'registration/register.html')

def charts(request):
    return render(request, 'charts.html')
def layoutsidenavlight(request):
    return render(request, 'layout-sidenav-light.html')
def layoutstatic(request):
    return render(request, 'layout-static.html')
def tables(request):
    return render(request, 'tables.html')

def listar_clientes(request):
    # URL de la API de clientes
    api_url = "https://1c6c-2001-1388-ae0-d5f8-5c34-f411-227f-aa55.ngrok-free.app/api/ventas/clientes/"  # Cambia por la URL real
    try:
        # Realizar la solicitud GET
        response = requests.get(api_url)
        response.raise_for_status()  # Lanza excepción si hay error
        clientes = response.json()  # Parsear respuesta como JSON
    except requests.exceptions.RequestException as e:
        # En caso de error, manejar excepción y pasar un mensaje al template
        clientes = []
        error = f"Error al consumir la API: {e}"
        return render(request, "core/clientes.html", {"clientes": clientes, "error": error})

    # Renderizar el template con la lista de clientes
    return render(request, "core/clientes.html", {"clientes": clientes})

def editar_cliente(request, cliente_id):
    # URL de la API para el cliente específico
    api_url = f"https://1c6c-2001-1388-ae0-d5f8-5c34-f411-227f-aa55.ngrok-free.app/api/ventas/clientes/{cliente_id}/"

    if request.method == "POST":
        try:
            # Obtener datos del formulario enviado
            datos_actualizados = {
                "username": request.POST.get("username"),
                "email": request.POST.get("email"),
                "first_name": request.POST.get("first_name"),
                "last_name": request.POST.get("last_name"),
                "phone": request.POST.get("phone"),
                "is_active": request.POST.get("is_active") == "on",
                "is_staff": request.POST.get("is_staff") == "on",
            }

            # Realizar solicitud PUT a la API para actualizar el cliente
            response = requests.put(api_url, json=datos_actualizados)
            response.raise_for_status()

            return redirect("listar_clientes")

        except requests.exceptions.RequestException as e:
            error = f"Error al actualizar cliente: {e}"
            return render(request, "core/editar_cliente.html", {"error": error})

    else:
        try:
            # Obtener datos del cliente desde la API
            response = requests.get(api_url)
            response.raise_for_status()

            cliente = response.json()

        except requests.exceptions.RequestException as e:
            cliente = {}
            error = f"Error al cargar datos del cliente: {e}"
            return render(request, "core/editar_cliente.html", {"cliente": cliente, "error": error})

        return render(request, "core/editar_cliente.html", {"cliente": cliente})

def delete_cliente(request, cliente_id):
    """
    Vista para eliminar un cliente dado su ID.
    """
    api_url = f"https://1c6c-2001-1388-ae0-d5f8-5c34-f411-227f-aa55.ngrok-free.app/api/ventas/clientes/{cliente_id}/"

    if request.method == "POST":
        try:
            # Realizar la solicitud DELETE
            response = requests.delete(api_url)
            response.raise_for_status()

            # Mostrar mensaje de éxito
            messages.success(request, "Cliente eliminado exitosamente.")
            return redirect("listar_clientes")

        except requests.exceptions.RequestException as e:
            # Manejar errores en la solicitud
            messages.error(request, f"Error al eliminar el cliente: {e}")
            return redirect("listar_clientes")

    # Renderizar página de confirmación
    return render(request, "core/delete_cliente.html", {"cliente_id": cliente_id})

def crear_cliente(request):
    if request.method == "POST":
        datos_actualizados = {
            "username": request.POST.get("username"),
            "email": request.POST.get("email"),
            "first_name": request.POST.get("first_name"),
            "last_name": request.POST.get("last_name"),
            "phone": request.POST.get("phone"),
            "is_active": request.POST.get("is_active") == "on",
            "is_staff": request.POST.get("is_staff") == "on",
        }

        api_url = "https://1c6c-2001-1388-ae0-d5f8-5c34-f411-227f-aa55.ngrok-free.app/api/ventas/clientes/"

        try:
            # Enviar solicitud POST a la API
            response = requests.post(api_url, json=datos_actualizados)
            response.raise_for_status()  # Lanza excepción si hay error

            # Redireccionar después de crear el cliente
            return redirect('listar_clientes')

        except requests.exceptions.RequestException as e:
            error = f"Error al crear el cliente: {e}"
            return render(request, "core/crear_cliente.html", {"error": error})

    return render(request, "core/crear_cliente.html")

def obtener_ventas(request):
    # URL de la API externa de ventas
    api_url = "https://1c6c-2001-1388-ae0-d5f8-5c34-f411-227f-aa55.ngrok-free.app/api/ventas/ventas/"

    # Realiza la solicitud GET a la API externa
    response = requests.get(api_url)
    
    if response.status_code == 200:
        ventas = response.json()
    else:
        ventas = []
    return render(request, 'core/ventas.html', {'ventas': ventas})

def detalle_venta(request, venta_id):
    # URL de la API externa para obtener el detalle de una venta específica
    api_url = f"https://1c6c-2001-1388-ae0-d5f8-5c34-f411-227f-aa55.ngrok-free.app/api/ventas/ventas/{venta_id}/"

    try:
        # Realizar la solicitud GET
        response = requests.get(api_url)
        response.raise_for_status()  # Lanza excepción si hay error
        venta = response.json()  # Parsear respuesta como JSON

    except requests.exceptions.RequestException as e:
        venta = None
        error = f"Error al consumir la API: {e}"
        return render(request, "core/detalle_venta.html", {"venta": venta, "error": error})
    
    # Renderizar el template con el detalle de la venta
    return render(request, "core/detalle_venta.html", {"venta": venta})


def listar_productos(request):
    # URLs de las APIs externas
    api_productos_url = "https://inventario-django-production.up.railway.app/api/productos/"
    api_categorias_url = "https://inventario-django-production.up.railway.app/api/categorias/"
    api_proveedores_url = "https://inventario-django-production.up.railway.app/api/proveedores/"

    try:
        # Obtener la lista de productos
        response_productos = requests.get(api_productos_url)
        response_productos.raise_for_status()
        productos = response_productos.json()

        # Obtener la lista de categorías
        response_categorias = requests.get(api_categorias_url)
        response_categorias.raise_for_status()
        categorias = {categoria["id"]: categoria["nombre"] for categoria in response_categorias.json()}

        # Obtener la lista de proveedores
        response_proveedores = requests.get(api_proveedores_url)
        response_proveedores.raise_for_status()
        proveedores = {proveedor["id"]: proveedor for proveedor in response_proveedores.json()}

        # Enriquecer los datos de productos con nombres de categorías y proveedores
        for producto in productos:
            producto["categoria_nombre"] = categorias.get(producto["categoria"], "Desconocida")
            proveedor = proveedores.get(producto["proveedor"], {"nombre": "Desconocido", "contacto": "Desconocido"})
            producto["proveedor_nombre"] = proveedor["nombre"]
            producto["proveedor_contacto"] = proveedor["contacto"]

    except requests.exceptions.RequestException as e:
        # Maneja errores en la comunicación con las APIs
        productos = []
        error = f"Error al consumir la API: {e}"
        return render(request, "core/productos.html", {"productos": productos, "error": error})

    # Renderiza la plantilla con los productos enriquecidos
    return render(request, "core/productos.html", {"productos": productos})

def detalle_producto(request, producto_id):
    # URL de la API externa
    api_url_producto = f"https://inventario-django-production.up.railway.app/api/productos/{producto_id}/"
    api_url_categoria = "https://inventario-django-production.up.railway.app/api/categorias/"
    api_url_proveedor = "https://inventario-django-production.up.railway.app/api/proveedores/"

    try:
        # Obtener los detalles del producto
        response_producto = requests.get(api_url_producto)
        response_producto.raise_for_status()
        producto = response_producto.json()

        # Obtener detalles de la categoría
        response_categoria = requests.get(f"{api_url_categoria}{producto['categoria']}/")
        response_categoria.raise_for_status()
        categoria = response_categoria.json()

        # Obtener detalles del proveedor
        response_proveedor = requests.get(f"{api_url_proveedor}{producto['proveedor']}/")
        response_proveedor.raise_for_status()
        proveedor = response_proveedor.json()

        # Enriquecer el producto con nombres de categoría y proveedor
        producto["categoria_nombre"] = categoria["nombre"]
        producto["proveedor_nombre"] = proveedor["nombre"]
        producto["proveedor_contacto"] = proveedor["contacto"]

    except requests.exceptions.RequestException as e:
        error = f"Error al consumir la API: {e}"
        return render(request, "core/detalle_producto.html", {"producto": None, "error": error})

    # Renderizar la plantilla con el producto enriquecido
    return render(request, "core/detalle_producto.html", {"producto": producto})

def obtener_nombres_clientes(request):
    api_clientes_url = "https://1c6c-2001-1388-ae0-d5f8-5c34-f411-227f-aa55.ngrok-free.app/api/ventas/clientes/"
    api_productos_url = "https://inventario-django-production.up.railway.app/api/productos/"

    try:
        # Obtener clientes
        clientes_response = requests.get(api_clientes_url)
        clientes_response.raise_for_status()
        clientes = clientes_response.json()

        # Obtener productos
        productos_response = requests.get(api_productos_url)
        productos_response.raise_for_status()
        productos = productos_response.json()

        if not clientes:
            messages.warning(request, "No hay clientes disponibles.")
        if not productos:
            messages.warning(request, "No hay productos disponibles.")

    except requests.exceptions.RequestException as e:
        messages.error(request, f"Error al cargar datos: {e}")
        return redirect("index")

    return render(request, "core/crear_venta.html", {"clientes": clientes, "productos": productos})
def crear_venta(request):
    if request.method != "POST":
        messages.warning(request, "Método no permitido.")
        return redirect("obtener_nombres_clientes")

    api_ventas_url = "https://1c6c-2001-1388-ae0-d5f8-5c34-f411-227f-aa55.ngrok-free.app/api/ventas/ventas/"
    try:
        # Obtener datos del formulario
        cliente_id = request.POST.get("cliente")
        productos = request.POST.getlist("producto[]")
        cantidades = request.POST.getlist("cantidad[]")

        if not cliente_id or not productos or not cantidades:
            messages.error(request, "Todos los campos son obligatorios.")
            return redirect("obtener_nombres_clientes")

        # Construir el payload
        items = [
            {"product_id": producto, "quantity": int(cantidad)}  # product_id como string para UUIDs
            for producto, cantidad in zip(productos, cantidades)
        ]

        payload = {
            "cliente_id": int(cliente_id),  # Asumimos que cliente_id sigue siendo un entero
            "address": "123 Main Street",
            "is_paid": True,
            "items": items,
        }

        # Enviar solicitud a la API
        response = requests.post(api_ventas_url, json=payload)
        if response.status_code == 201:  # Verificar éxito
            messages.success(request, "Venta creada exitosamente.")
            return redirect("obtener_ventas")
        else:
            # Capturar detalles del error desde la respuesta
            error_detail = response.json().get("detail", "Error desconocido")
            messages.error(request, f"Error al crear la venta: {error_detail}")
            return redirect("obtener_nombres_clientes")

    except requests.exceptions.RequestException as e:
        # Manejar excepciones de solicitudes
        messages.error(request, f"Error al procesar la venta: {e}")
        return redirect("obtener_nombres_clientes")
