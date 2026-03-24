from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Cliente


class ClienteListView(ListView):
    model = Cliente
    template_name = 'clientes/cliente_list.html'
    context_object_name = 'clientes'


class ClienteDetailView(DetailView):
    model = Cliente
    template_name = 'clientes/cliente_detail.html'
    context_object_name = 'cliente'


class ClienteCreateView(CreateView):
    model = Cliente
    template_name = 'clientes/cliente_form.html'
    fields = ['nombre', 'apellido', 'email', 'telefono', 'direccion']
    success_url = reverse_lazy('clientes:lista')


class ClienteUpdateView(UpdateView):
    model = Cliente
    template_name = 'clientes/cliente_form.html'
    fields = ['nombre', 'apellido', 'email', 'telefono', 'direccion']
    success_url = reverse_lazy('clientes:lista')


class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'clientes/cliente_confirm_delete.html'
    success_url = reverse_lazy('clientes:lista')
