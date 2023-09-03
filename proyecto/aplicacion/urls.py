from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home, name="home" ),
    path('sobremi/', sobremi, name="sobremi" ),
    path('empresa/', SearchResultsViewEmpresa.as_view(), name="empresa" ),
    path('crear_empresa/', EmpresaCreate.as_view(), name="crear_empresa" ),    
    path('actualizar_empresa/<int:pk>/', EmpresaUpdate.as_view(), name="actualizar_empresa" ),
    path('eliminar_empresa/<int:pk>/', EmpresaDelete.as_view(), name="eliminar_empresa" ),

    # path('garantia/', garantia, name="garantia" ),
    # path('actualizargarantia/<id_garantia>/', actualizargarantia, name="actualizargarantia" ),
    # path('eliminargarantia/<id_garantia>/', eliminargarantia, name="eliminargarantia" ),
    # path('creargarantia/', creargarantia, name="creargarantia" ),

    path('clientes/', SearchResultsViewCliente.as_view(), name="clientes" ),
    path('crear_cliente/', ContactoCreate.as_view(), name="crear_cliente" ),    
    path('actualizar_cliente/<int:pk>/', ContactoUpdate.as_view(), name="actualizar_cliente" ),
    path('eliminar_cliente/<int:pk>/', ContactoDelete.as_view(), name="eliminar_cliente" ),

    path('garantia/', SearchResultsViewGarantia.as_view(), name="garantia" ),
    path('crear_garantia/', GarantiaCreate.as_view(), name="crear_garantia" ),    
    path('actualizar_garantia/<int:pk>/', GarantiaUpdate.as_view(), name="actualizar_garantia" ),
    path('eliminar_garantia/<int:pk>/', GarantiaDelete.as_view(), name="eliminar_garantia" ),

    path('sucursal/', SearchResultsViewSucursal.as_view(), name="sucursal" ),
    path('crear_sucursal/', SucursalCreate.as_view(), name="crear_sucursal" ),    
    path('actualizar_sucursal/<int:pk>/', SucursalUpdate.as_view(), name="actualizar_sucursal" ),
    path('eliminar_sucursal/<int:pk>/', SucursalDelete.as_view(), name="eliminar_sucursal" ),

    path('login/', login_request, name="login" ),
    path('logout/', LogoutView.as_view(template_name="aplicacion/home.html"), name="logout" ),
    path('registro/', register, name="registro" ),
    path('editar_perfil/', editarPerfil, name="editar_perfil" ),
    path('agregar_avatar/', agregarAvatar, name="agregar_avatar" ),


]