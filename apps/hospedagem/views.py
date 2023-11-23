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
from apps.cliente.models import Cliente

from apps.quarto.models import Quarto

from .forms import HospedagemFilterForm, HospedagemForm

from .models import Hospedagem

# Create your views here.

class Index(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_hospedagens"] = Hospedagem.objects.count()
        context["total_clientes"] = Cliente.objects.count()
        context["total_quartos"] = Quarto.objects.count()
        return context

class HospedagemCriar(CreateView):
    model = Hospedagem
    form_class = HospedagemForm
    template_name = "hospedagem/form.html"
    success_url = reverse_lazy("hospedagem_urls:hospedagem_listar")


class HospedagemListar(ListView):
    model = Hospedagem
    template_name = "hospedagem/hospedagens.html"
    context_object_name = "hospedagens"
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = HospedagemFilterForm(self.request.GET or None)
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        self.form = HospedagemFilterForm(self.request.GET or None)

        if self.form.is_valid():
            if self.form.cleaned_data.get('data_entrada'):
                queryset = queryset.filter(data_entrada__icontains=self.form.cleaned_data['data_entrada'])
            if self.form.cleaned_data.get('data_saida'):
                queryset = queryset.filter(data_saida__icontains=self.form.cleaned_data['data_saida'])
            if self.form.cleaned_data.get('cliente'):
                queryset = queryset.filter(cliente=self.form.cleaned_data['cliente'])
            if self.form.cleaned_data.get('quarto'):
                queryset = queryset.filter(quarto=self.form.cleaned_data['quarto'])
        return queryset


class HospedagemEditar(UpdateView):
    model = Hospedagem
    form_class = HospedagemForm
    template_name = "hospedagem/form.html"
    success_url = reverse_lazy("hospedagem_urls:hospedagem_listar")
    pk_url_kwarg = "id"


class HospedagemDetalhar(DetailView):
    model = Hospedagem
    form_class = HospedagemForm
    template_name = "hospedagem/detalhar.html"
    success_url = reverse_lazy("hospedagem_urls:hospedagem_listar")
    pk_url_kwarg = "id"


class HospedagemDeletar(DeleteView):
    model = Hospedagem
    pk_url_kwarg = "id"
    template_name = "hospedagem/hospedagem_confirm_delete.html"
    success_url = reverse_lazy("hospedagem_urls:hospedagem_listar")

# def hospedagem_listar(request):
#     hospedagens = Hospedagem.objects.all()
#     return render(request, 'hospedagem/hospedagens.html', {'hospedagens': hospedagens})

# def hospedagem_detalhar(request, id):
#     hospedagem = get_object_or_404(Hospedagem, id=id)
#     return render(request, 'hospedagem/detalhar.html', {'hospedagem': hospedagem})

# def hospedagem_criar(request):
#     if request.method == 'POST':
#         form = HospedagemForm(request.POST)
#         if form.is_valid():
#             form.save()
#             form = HospedagemForm()
#             return redirect('hospedagem_listar')

#     else:
#         form = HospedagemForm()

#     return render(request, 'hospedagem/form.html', {'form': form})

# def hospedagem_editar(request, id):
#     hospedagem = get_object_or_404(Hospedagem, id=id)

#     if request.method == 'POST':
#         form = HospedagemForm(request.POST, instance=hospedagem)

#         if form.is_valid():
#             form.save()
#             return redirect('hospedagem_listar')
#     else:
#         form = HospedagemForm(instance=hospedagem)
        
#     return render(request, 'hospedagem/form.html', {'form': form})

# def hospedagem_remover(request, id):
#     hospedagem = get_object_or_404(Hospedagem, id=id)
#     hospedagem.delete()
#     return redirect('hospedagem_listar')
