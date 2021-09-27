from django.urls import reverse_lazy
from .models import Produto
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# LISTVIEW -> lista os registros
# CREATEVIEW -> criar os registros
# UPDATEVIEW -> atualiza os registros
# DELETEVIEW -> delete os registros


# Create your views here.
class IndexView(ListView):
    """
    Listagem dos produtos
    """
    model = Produto
    template_name = 'index.html'
    queryset = Produto.objects.all()  # similar os SELECT
    context_object_name = 'produtos'  # nome para ser usado para recuperar os dados no template


class CreateProdutoView(CreateView):
    """
    Registrando / criando registros (produtos)
    """
    model = Produto
    template_name = 'produto_form.html'
    fields = ['nome', 'preco']
    success_url = reverse_lazy('index')


class UpdateProdutoView(UpdateView):
    """
    Atualizando produtos
    """
    model = Produto
    template_name = 'produto_form.html'
    fields = ['nome', 'preco']
    success_url = reverse_lazy('index')


class DeleteProdutoView(DeleteView):
    """
    Deletando produto
    """
    model = Produto
    template_name = 'produto_del.html'  # tela de confirmação
    success_url = reverse_lazy('index')
