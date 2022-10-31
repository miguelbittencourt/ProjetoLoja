from telnetlib import STATUS
from django.shortcuts import redirect, render
from crudloja.form import ProdutoForm
# from crudloja.form import ProdutoForm
from crudloja.models import Produto
from django.core.paginator import Paginator

def home(request):
    data = {}
    all = Produto.objects.all()
    paginator = Paginator(all, 10)
    pages = request.GET.get('page')
    data['produtos'] = paginator.get_page(pages)
    return render(request, 'index.html', data)

def form(request):
    data = {}
    data['form'] = ProdutoForm()
    return render(request, 'form.html', data)

def create(request):
    form = ProdutoForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('home')
    else:
        return redirect('home', STATUS=400)

def delete(request, id):
    produto = Produto.objects.get(id=id)
    produto.delete()
    return redirect('home')

def edit(request, id):
    data = {}
    data['produto'] = Produto.objects.get(id=id)
    data['form'] = ProdutoForm(instance=data['produto'])
    return render(request, 'form.html', data)

def update(request, id):
    data = {}
    data['produto'] = Produto.objects.get(id=id)
    form = ProdutoForm(request.POST, instance=data['produto'])
    if form.is_valid():
         form.save()
         return redirect('home')

