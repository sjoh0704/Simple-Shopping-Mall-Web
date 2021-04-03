from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import ListView
from .forms import RegisterForm
from django.shortcuts import redirect
from .models import Order
# Create your views here.


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

class OrderList(ListView):
    model = Order
    template_name = 'order.html'
    context_object_name = "ordered_list"
