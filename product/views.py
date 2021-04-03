from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from .forms import RegisterForm
from .models import Product
from order.forms import RegisterForm as OrderForm
from django.utils.decorators import method_decorator
from fcuser.decorator import admin_required
# Create your views here.

class ProductList(ListView):
    model = Product
    template_name = 'product.html'

@method_decorator(admin_required, name="dispatch")
class ProductRegister(FormView):
    template_name = 'register_product.html'
    form_class = RegisterForm
    success_url = "/product"

class ProductDetail(DetailView):
    template_name = 'detail_product.html'
    queryset = Product.objects.all()
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = OrderForm(self.request)
        return context