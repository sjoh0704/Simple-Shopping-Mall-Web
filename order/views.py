from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import ListView
from .forms import RegisterForm
from django.shortcuts import redirect
from .models import Order
from django.utils.decorators import method_decorator  #데코레이터를 편하게 사용할 수 있게 해주는 함수
from fcuser.decorator import login_required, admin_required
# Create your views here.

@method_decorator(login_required, name = 'dispatch')  # 클래스가 시작될때 dispath함수가 제일먼저 시작된다고 한다. 그래서 dispath로 설정
class OrderCreate(FormView):

    form_class = RegisterForm
    success_url = "/product/"

    def form_invalid(self, form):
        return redirect('/product/' + str(form.product_id))


    # request라는 인자도 전달해서 폼클래스를 만들겠다. 
    def get_form_kwargs(self, **kwargs):
        kw =super().get_form_kwargs(** kwargs)
        kw.update({
            'request': self.request
        })
        return kw

@method_decorator(login_required, name = 'dispatch')
class OrderList(ListView):
    model = Order
    template_name = 'order.html'
    context_object_name = "ordered_list"

    # 사용자마다 다른 주문리스트를 보여주여야 하므로 
    # 이를 쿼리셋함수로 처리한다. listview는 self.request가 들어가 있는 듯하다. 
    def get_queryset(self, **kwargs):
        queryset = Order.objects.filter(fcuser__email=self.request.session.get('user'))
        return queryset

