from django.urls import path
from .views import *

app_name = 'quarto_urls'

urlpatterns = [
    path('quarto/listar', QuartoListar.as_view(),name='quarto_listar'),
    path('quarto/', QuartoCriar.as_view(),name='quarto_criar'),
    path('quarto/detalhar/<int:id>/', QuartoDetalhar.as_view(), name='quarto_detalhar'),
    path('quarto/editar/<int:id>/', QuartoEditar.as_view(), name='quarto_editar'),
    path('quarto/remover/<int:id>/', QuartoDeletar.as_view(),name='quarto_remover'),
]