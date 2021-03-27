from django.db import models

# Create your models here.

class Order(models.Model):
    fcuser = models.ForeignKey("fcuser.Fcuser", verbose_name=" 사용자" , on_delete=models.CASCADE)
    product = models.ForeignKey('product.Product', verbose_name = "상품", on_delete=models.CASCADE)
    quantity = models.IntegerField(verbose_name = "수량") 
    register_date = models.DateTimeField(verbose_name = "등록 날짜", auto_now_add=True)



    def __str__(self):
        return str(self.fcuser) + ' ' + str(self.product)
    
    class Meta:
        db_table = "order"
        verbose_name = "주문"
        verbose_name_plural = "주문"