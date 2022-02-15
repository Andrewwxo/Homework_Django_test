from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from myshop.models import Product, ProductKind


def index(request):
    return render(request, 'myshop/index.html')


def product_list(request):
    products = Product.objects.all()
    context = {
        'p_title': 'Shop of products',
        'product_list': products
    }
    return render(request, 'myshop/product_list.html', context=context)


# class ProductsListView(ListView):
#     model = Product
#

    # template_name = 'myshop/product_list.html'
    # context_object_name = 'product_list'
    # paginate_by = 5


# def about(request):
#     return render(request, 'myshop/about.html')


class ProductKindCreateView(CreateView):
    model = ProductKind
    success_url = reverse_lazy('myshop:product_list')
    fields = ('name',)
