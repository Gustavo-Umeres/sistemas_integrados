from pyexpat.errors import messages
from django.shortcuts import get_object_or_404, render, redirect
import requests
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from .forms import *

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
    api_url = "https://5c2c-38-253-159-56.ngrok-free.app/api/ventas/clientes/"  # Cambia por la URL real
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
    api_url = f"https://5c2c-38-253-159-56.ngrok-free.app/api/ventas/clientes/{cliente_id}/"

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
    api_url = f"https://5c2c-38-253-159-56.ngrok-free.app/api/ventas/clientes/{cliente_id}/"

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

        api_url = "https://5c2c-38-253-159-56.ngrok-free.app/api/ventas/clientes/"

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
    api_url = "https://5c2c-38-253-159-56.ngrok-free.app/api/ventas/ventas/"

    # Realiza la solicitud GET a la API externa
    response = requests.get(api_url)
    
    if response.status_code == 200:
        ventas = response.json()
    else:
        ventas = []
    return render(request, 'core/ventas.html', {'ventas': ventas})

def detalle_venta(request, venta_id):
    # URL de la API externa para obtener el detalle de una venta específica
    api_url = f"https://5c2c-38-253-159-56.ngrok-free.app/api/ventas/ventas/{venta_id}/"

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
    # URL de la API externa de productos
    api_url = "http://127.0.0.1:8081/api/productos/"  # Cambia esta URL por la de tu API real

    try:
        # Realiza la solicitud GET
        response = requests.get(api_url)
        response.raise_for_status()  # Lanza una excepción si ocurre un error
        productos = response.json()  # Parsea la respuesta a formato JSON
    except requests.exceptions.RequestException as e:
        # Maneja errores al consumir la API
        productos = []
        error = f"Error al consumir la API: {e}"
        return render(request, "core/productos.html", {"productos": productos, "error": error})

    # Renderiza el template con la lista de productos
    return render(request, "core/productos.html", {"productos": productos})

def detalle_producto(request, producto_id):
    # URL de la API externa para obtener el detalle de una venta específica
    api_url = f"http://127.0.0.1:8081/api/productos/{producto_id}/"

    try:
        # Realizar la solicitud GET
        response = requests.get(api_url)
        response.raise_for_status()  # Lanza excepción si hay error
        producto = response.json()  # Parsear respuesta como JSON

    except requests.exceptions.RequestException as e:
        venta = None
        error = f"Error al consumir la API: {e}"
        return render(request, "core/detalle_producto.html", {"producto": producto, "error": error})
    
    # Renderizar el template con el detalle de la venta
    return render(request, "core/detalle_producto.html", {"producto": producto})


def obtener_nombres_clientes(request):
    # URL de la API de clientes
    api_url = "https://5c2c-38-253-159-56.ngrok-free.app/api/ventas/clientes/"  # Cambia por la URL real
    try:
        # Realizar la solicitud GET
        response = requests.get(api_url)
        response.raise_for_status()  # Lanza excepción si hay error
        clientes = response.json()  # Parsear respuesta como JSON
        
        # Crear una lista con los nombres completos
        nombres_completos = [f"{cliente['first_name']} {cliente['last_name']}" for cliente in clientes]
    except requests.exceptions.RequestException as e:
        # En caso de error, manejar excepción y pasar un mensaje al template
        nombres_completos = []
        error = f"Error al consumir la API: {e}"
        return render(request, "core/nombres_clientes.html", {"nombres_completos": nombres_completos, "error": error})

    # Renderizar el template con la lista de nombres completos
    return render(request, "core/crear_venta.html", {"nombres_completos": nombres_completos})


