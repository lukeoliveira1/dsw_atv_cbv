from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (
    CreateView,
    UpdateView,
    ListView,
    DetailView,
    DeleteView,
    TemplateView,
)
from django.urls import reverse_lazy

from .forms import ClienteFilterForm, ClienteForm

from .models import Cliente


# Create your views here.
class ClienteCriar(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = "cliente/form.html"
    success_url = reverse_lazy("cliente_urls:cliente_listar")


class ClienteListar(ListView):
    model = Cliente
    template_name = "cliente/clientes.html"
    context_object_name = "clientes"
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ClienteFilterForm(self.request.GET or None)
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        self.form = ClienteFilterForm(self.request.GET or None)

        if self.form.is_valid():
            if self.form.cleaned_data.get('nome'):
                queryset = queryset.filter(nome__icontains=self.form.cleaned_data['nome'])
        return queryset


class ClienteEditar(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = "cliente/form.html"
    success_url = reverse_lazy("cliente_urls:cliente_listar")
    pk_url_kwarg = "id"


class ClienteDetalhar(DetailView):
    model = Cliente
    form_class = ClienteForm
    template_name = "cliente/detalhar.html"
    success_url = reverse_lazy("cliente_urls:cliente_listar")
    pk_url_kwarg = "id"


class ClienteDeletar(DeleteView):
    model = Cliente
    pk_url_kwarg = "id"
    template_name = "cliente/cliente_confirm_delete.html"
    success_url = reverse_lazy("cliente_urls:cliente_listar")
