from .models import Fcuser
from django.shortcuts import redirect
def login_required(function):
    def wrap(request, *args, **kwards):  # 데코레이팅 당하는 함수의 인수까지 고려해주어야 하므로  
        email = request.session.get('user')
        if email == None or not email:
            return redirect('/login')

        return function(request, *args, **kwards)
    return wrap

def admin_required(function):
    def wrap(request, *args, **kwards):
        email = request.session.get('user')
        if email == None or not email:
            print("레벨!!!", email)
            return redirect('/login')
        
        user = Fcuser.objects.get(email=email)
        print("레벨!!!",user.level)
        if user.level != 'admin':
            return redirect('/')
        return function(request, *args, **kwards)
    return wrap
