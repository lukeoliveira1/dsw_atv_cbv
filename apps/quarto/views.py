from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (
    CreateView,
    UpdateView,
    ListView,
    DetailView,
    DeleteView,
)
from django.urls import reverse_lazy
from apps.quarto.forms import QuartoFilterForm, QuartoForm

from apps.quarto.models import Quarto


class QuartoCriar(CreateView):
    model = Quarto
    form_class = QuartoForm
    template_name = "quarto/form.html"
    success_url = reverse_lazy("quarto_urls:quarto_listar")


class QuartoListar(ListView):
    model = Quarto
    template_name = "quarto/quartos.html"
    context_object_name = "quartos"
    paginate_by = 2
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = QuartoFilterForm(self.request.GET or None)
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        self.form = QuartoFilterForm(self.request.GET or None)

        if self.form.is_valid():
            if self.form.cleaned_data.get('apartamento'):
                queryset = queryset.filter(apartamento__icontains=self.form.cleaned_data['apartamento'])
        return queryset

class QuartoEditar(UpdateView):
    model = Quarto
    form_class = QuartoForm
    template_name = "quarto/form.html"
    success_url = reverse_lazy("quarto_urls:quarto_listar")
    pk_url_kwarg = "id"


class QuartoDetalhar(DetailView):
    model = Quarto
    form_class = QuartoForm
    template_name = "quarto/detalhar.html"
    success_url = reverse_lazy("quarto_urls:quarto_listar")
    pk_url_kwarg = "id"


class QuartoDeletar(DeleteView):
    model = Quarto
    pk_url_kwarg = "id"
    template_name = "quarto/quarto_confirm_delete.html"
    success_url = reverse_lazy("quarto_urls:quarto_listar")
