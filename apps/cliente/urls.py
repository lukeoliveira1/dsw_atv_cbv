from django.urls import path
from .views import *

app_name = 'cliente_urls'

urlpatterns = [
    path('cliente/listar', ClienteListar.as_view(),name='cliente_listar'),
    path('cliente/', ClienteCriar.as_view(),name='cliente_criar'),
    path('cliente/detalhar/<int:id>/', ClienteDetalhar.as_view(), name='cliente_detalhar'),
    path('cliente/editar/<int:id>/', ClienteEditar.as_view(), name='cliente_editar'),
    path('cliente/remover/<int:id>/', ClienteDeletar.as_view(),name='cliente_remover'),
]