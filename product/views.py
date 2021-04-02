from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from .forms import RegisterForm
from .models import Product

# Create your views here.

class ProductList(ListView):
    model = Product
    template_name = 'product.html'

class ProductRegister(FormView):
    template_name = 'register_product.html'
    form_class = RegisterForm
    success_url = "/product"

class ProductDetail(DetailView):
    template_name = 'detail_product.html'
    queryset = Product.objects.all()
    context_object_name = 'product'