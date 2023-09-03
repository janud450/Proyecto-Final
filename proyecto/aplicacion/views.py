from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy

from django import *

from .models import *
from .forms import *

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import *


from search_views.search import SearchListView
from search_views.filters import BaseFilter

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth       import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, "aplicacion/home.html")

@login_required
def clientes(request):
    contexto = {'clientes': Contacto.objects.all(), 'titulo': 'Reporte Clientes' }
    return render(request, "aplicacion/clientes.html", contexto)
@login_required
def empresa(request):
    contexto = {'empresas': Empresa.objects.all(), 'titulo': 'Reporte de Empresas' }
    return render(request, "aplicacion/empresa.html", contexto)
@login_required
def garantia(request):
    contexto = {'garantias': Garantia.objects.all(), 'titulo': 'Reporte de Garantías' }
    return render(request, "aplicacion/garantia.html", contexto)

def sobremi(request):
    return render(request, "aplicacion/SobreMi.html")


# def empresaform(request):
#     if request.method == "POST":
#         miForm = empresaForm(request.POST)
#         if miForm.is_valid():
#             empresa_nombre = miForm.cleaned_data.get('nombre')
#             empresa_nit = miForm.cleaned_data.get('nit')
#             empresa = Empresa(nombre=empresa_nombre,nit=empresa_nit)
#             empresa.save()
#             return render(request, "aplicacion/ingreso_exitoso.html")
#     else:

#         miForm = empresaForm()
    
#     return render(request, "aplicacion/empresaform.html", {"form": miForm })
             
#  #___________________________________CRUD            

# @login_required   
# def actualizargarantia(request, id_garantia):
#     garantia = Garantia.objects.get(id=id_garantia)
#     if request.method == "POST":
#         miForm = GarantiaForm(request.POST)
#         if miForm.is_valid():
#             garantia.banco = miForm.cleaned_data.get('banco')
#             garantia.contrato = miForm.cleaned_data.get('contrato')
#             garantia.valor = miForm.cleaned_data.get('valor')
#             garantia.fecha_inicial = miForm.cleaned_data.get('fecha_inicial') 
#             garantia.fecha_final = miForm.cleaned_data.get('fecha_final') 
#             garantia.save()
#             return redirect(reverse_lazy('garantia'))   
#     else:
#         miForm = GarantiaForm(initial={
#             'banco': garantia.banco,
#             'contrato': garantia.contrato,
#             'valor': garantia.valor,
#             'fecha_inicial': garantia.fecha_inicial,
#             'fecha_final': garantia.fecha_final,
#         })
#     return render(request, "aplicacion/GarantiaForm.html", {'form': miForm})
# @login_required
# def eliminargarantia(request, id_garantia):
#     garantia = Garantia.objects.get(id=id_garantia)
#     garantia.delete()
#     return redirect(reverse_lazy('garantia'))

# @login_required
# def creargarantia(request):    
#     if request.method == "POST":
#         miForm = GarantiaForm(request.POST)
#         if miForm.is_valid():
#             p_banco = miForm.cleaned_data.get('banco')
#             p_contrato = miForm.cleaned_data.get('contrato')
#             p_valor = miForm.cleaned_data.get('valor')
#             p_fecha_inicial = miForm.cleaned_data.get('fecha_inicial')
#             p_fecha_final = miForm.cleaned_data.get('fecha_final')
#             garantia = Garantia(banco=p_banco, 
#                                 contrato = p_contrato,
#                                 valor = p_valor,
#                                 fecha_inicial = p_fecha_inicial,
#                                 fecha_final = p_fecha_final
#                              )
#             garantia.save()
#             return redirect(reverse_lazy('garantia'))
#     else:
#         miForm = GarantiaForm()

#     return render(request, "aplicacion/GarantiaForm.html", {"form":miForm})

#____________________ Class Based View  Clientes

class ContactoList(LoginRequiredMixin,ListView):
    model = Contacto

class ContactoCreate(LoginRequiredMixin,CreateView):
    model = Contacto
    fields = ['nombre', 'apellido', 'email']
    success_url = reverse_lazy('clientes')

class ContactoUpdate(LoginRequiredMixin,UpdateView):
    model = Contacto
    fields = ['nombre', 'apellido', 'email']
    success_url = reverse_lazy('clientes')

class ContactoDelete(LoginRequiredMixin,DeleteView):
    model = Contacto
    success_url = reverse_lazy('clientes')

class ClienteFilter(LoginRequiredMixin,BaseFilter):
    search_fields = {
        'search_text' : ['nombre', 'apellido','email'],
    }

class SearchResultsViewCliente(LoginRequiredMixin,SearchListView):
    model = Contacto
    paginate_by = 30
    template_name = "aplicacion/contacto_list.html"
    form_class = ClienteSearchForm
    filter_class = ClienteFilter

#____________________ Class Based View  Garantías

class GarantiaList(LoginRequiredMixin,ListView):
    model = Garantia

class GarantiaCreate(LoginRequiredMixin,CreateView):
    model = Garantia
    fields = ['banco', 'contrato', 'valor', 'fecha_inicial','fecha_final']
    success_url = reverse_lazy('garantia')

class GarantiaUpdate(LoginRequiredMixin,UpdateView):
    model = Garantia
    fields = ['banco', 'contrato', 'valor', 'fecha_inicial','fecha_final']
    success_url = reverse_lazy('garantia')

class GarantiaDelete(LoginRequiredMixin,DeleteView):
    model = Garantia
    success_url = reverse_lazy('garantia')


class GarantiaFilter(LoginRequiredMixin,BaseFilter):
    search_fields = {
        'search_text' : ['banco', 'contrato','fecha_final', 'valor'],
        'search_fecha_exact' : { 'operator' : '__lte', 'fields' : ['fecha_final'] },
    }

class SearchResultsViewGarantia(LoginRequiredMixin,SearchListView):
    model = Garantia
    paginate_by = 30
    template_name = "aplicacion/garantia_list.html"
    form_class = GarantiaSearchForm
    filter_class = GarantiaFilter


#____________________ Class Based View  Empresas

class EmpresaList(LoginRequiredMixin,ListView):
    model = Empresa

class EmpresaCreate(LoginRequiredMixin,CreateView):
    model = Empresa
    fields = ['nombre', 'nit']
    success_url = reverse_lazy('empresa')

class EmpresaUpdate(LoginRequiredMixin,UpdateView):
    model = Empresa
    fields = ['nombre','nit']
    success_url = reverse_lazy('empresa')

class EmpresaDelete(LoginRequiredMixin,DeleteView):
    model = Empresa
    success_url = reverse_lazy('empresa')


class EmpresaFilter(LoginRequiredMixin,BaseFilter):
    search_fields = {
        'search_text' : ['nombre', 'nit'],
    }

class SearchResultsViewEmpresa(LoginRequiredMixin,SearchListView):
    model = Empresa
    paginate_by = 30
    template_name = "aplicacion/empresa_list.html"
    form_class = EmpresaSearchForm
    filter_class = EmpresaFilter
#____________________ Class Based View  Sucursal

class SucursalList(LoginRequiredMixin,ListView):
    model = Sucursal

class SucursalCreate(LoginRequiredMixin,CreateView):
    model = Sucursal
    fields = ['ciudad', 'cantidad_empleados']
    success_url = reverse_lazy('sucursal')

class SucursalUpdate(LoginRequiredMixin,UpdateView):
    model = Sucursal
    fields = ['ciudad','cantidad_empleados']
    success_url = reverse_lazy('empresa')

class SucursalDelete(LoginRequiredMixin,DeleteView):
    model = Sucursal
    success_url = reverse_lazy('sucursal')


class SucursalFilter(LoginRequiredMixin,BaseFilter):
    search_fields = {
        'search_text' : ['ciudad', 'cantidad_empleados'],
    }

class SearchResultsViewSucursal(LoginRequiredMixin,SearchListView):
    model = Sucursal
    paginate_by = 30
    template_name = "aplicacion/sucursal_list.html"
    form_class = SucursalSearchForm
    filter_class = SucursalFilter

#__________________ Login / Logout / Registro
# 

def login_request(request):
    if request.method == "POST":
        miForm = AuthenticationForm(request, data=request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            password = miForm.cleaned_data.get('password')
            user = authenticate(username=usuario, password=password)
            if user is not None:
                login(request, user)

                try:
                    avatar = Avatar.objects.get(user=request.user.id).imagen.url
                except:
                    avatar = "/media/avatares/.png"
                finally:
                    request.session["avatar"] = avatar

                return render(request, "aplicacion/base.html", {'mensaje': f'Bienvenido a nuestro sitio {usuario}'})
            else:
                return render(request, "aplicacion/login.html", {'form': miForm, 'mensaje': f'Los datos son inválidos'})
        else:
            return render(request, "aplicacion/login.html", {'form': miForm, 'mensaje': f'Los datos son inválidos'})

    miForm =   AuthenticationForm()      

    return render(request, "aplicacion/login.html", {"form":miForm})     


def register(request):
    if request.method == "POST":
        miForm = RegistroUsuariosForm(request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            miForm.save()
            return render(request, "aplicacion/base.html")
    else:
        miForm =   RegistroUsuariosForm()      
    return render(request, "aplicacion/registro.html", {"form":miForm}) 

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            usuario.email = form.cleaned_data.get('email')
            usuario.password1 = form.cleaned_data.get('password1')
            usuario.password2 = form.cleaned_data.get('password2')
            usuario.first_name = form.cleaned_data.get('first_name')
            usuario.last_name = form.cleaned_data.get('last_name')
            usuario.save()
            return render(request,"aplicacion/base.html")
        else:
            return render(request,"aplicacion/editarPerfil.html", {'form': form, 'usuario': usuario.username})
    else:
        form = UserEditForm(instance=usuario)
    return render(request, "aplicacion/editarPerfil.html", {'form': form, 'usuario': usuario.username})

@login_required
def agregarAvatar(request):
    if request.method == "POST":
        form = AvatarFormulario(request.POST, request.FILES) # Diferente a los forms tradicionales
        if form.is_valid():
            u = User.objects.get(username=request.user)

            # ____ Para borrar el avatar viejo
            avatarViejo = Avatar.objects.filter(user=u)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()

            # ____ Guardar el nuevo
            avatar = Avatar(user=u, imagen=form.cleaned_data['imagen'])
            avatar.save()

            # ___ Hago que la url de la imagen viaje en el request
            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session["avatar"] = imagen
            return render(request,"aplicacion/base.html")
    else:
        form = AvatarFormulario()
    return render(request, "aplicacion/agregarAvatar.html", {'form': form })

