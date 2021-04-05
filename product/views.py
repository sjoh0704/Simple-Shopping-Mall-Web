from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from rest_framework import generics
from rest_framework import mixins
from .forms import RegisterForm
from .models import Product
from order.forms import RegisterForm as OrderForm
from django.utils.decorators import method_decorator
from fcuser.decorator import admin_required
from .serializers import ProductSerializer


# 믹스인을 상속받음으로써 겟에 대한 리스트 동작을 만들 수 있다. 
# 포스트에 대한 동작또한 믹스인에서 필요한 기능을 찾아 만들 수 있음
class ProductListApi(generics.GenericAPIView, mixins.ListModelMixin):
    
    # 시리얼라이즈를 등록하기
    serializer_class = ProductSerializer
    
    # 어떤 데이터를 가지고 올것인지 명시
    def get_queryset(self):
        return Product.objects.all().order_by('id')

    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
        # 믹스인을 상속받음으로써 self.list를 사용

class ProductDetailApi(generics.GenericAPIView, mixins.RetrieveModelMixin):
    
    # 시리얼라이즈를 등록하기
    serializer_class = ProductSerializer
    
    # 어떤 데이터를 가지고 올것인지 명시
    def get_queryset(self):
        return Product.objects.all().order_by('id')
        # 프로덕트 하나에 대한 것을 가져와여하는 왜 모두 가져오냐? -> 이것은 retrieve믹스인이 
        # 자동으로  pk에 따른 프로덕트를 가져오게 되어있음 

    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
        # 상세보기 믹스인을 상속받음으로써 self.retrieve를 사용


class ProductList(ListView):
    model = Product
    template_name = 'product.html'

@method_decorator(admin_required, name="dispatch")
class ProductRegister(FormView):
    template_name = 'register_product.html'
    form_class = RegisterForm
    success_url = "/product"


    def form_valid(self, form):
        product = Product(name = form.data.get("name"), 
        price = form.data.get("price"), 
        description= form.data.get("description"), 
        stock = form.data.get("stock"))
        product.save()
        return super().form_valid(form)

class ProductDetail(DetailView):
    template_name = 'detail_product.html'
    queryset = Product.objects.all()
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = OrderForm(self.request)
        return context