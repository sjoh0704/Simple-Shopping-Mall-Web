from django import forms
from .models import Order
from product.models import Product
from fcuser.models import Fcuser
from django.db import transaction

class RegisterForm(forms.Form):
    
    quantity = forms.IntegerField(
        error_messages={
            'required': "수량을 입력해주세요"
    }, label="수량")


    # 상품정보는 내가 입력하는 게 아니며 id가 된다
    # 사용자에게는 보여지지 않게 만드려고 hiddeninput으로
    product = forms.IntegerField(
         label="상품 정보",
         widget=forms.Textarea)


    # 상품구매 request를 전달해주어야 하므로
    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    def clean(self):
        cleaned_data = super().clean()
        quantity = cleaned_data.get("quantity")
        product_id = cleaned_data.get("product")
        # 쿼리문제면 키와 value가 맞지 않는다는 것

        # transaction을 이용하여 주문이 들어가면서 상품 재고도 줄어들게 할것이다.
        # 일련의 여러 동작을 하나의 동작으로 취급하겠다. 전체가 성공해야 동작이 돌아가고 
        # 하나라도 실패하면 돌아가지 않는다.(트랜잭션은 데이터베이스에서 제공하는 기능)

        if not(quantity and product_id):
            self.add_error('quantity', "수량을 입력해주세요")
            self.add_error('product', '제품을 선택해주세요')