from rest_framework import serializers
from .models import Product


# 시리얼라이즈는 모델을 json으로 바꾸어 준다.
class ProductSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = Product
        fields = "__all__"
        # 모든 필드를 가지고 온다. 만약 써주지 않으면 모든 필드를 가지고 옴