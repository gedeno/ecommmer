from django.forms import ModelFrom
from .models import Normal_product,Phone_product,Laptop_product

class Normal_product_form(ModelFrom):
    class Meta:
        model = Normal_product
        fields = '__all__'
class Phone_product_form(ModelFrom):
    class Meta:
        model = Phone_product
        fields = ['product_display','product_camera','product_battery','product_ram','product_storage']
class Laptop_product_form(ModelFrom):
    class Meta:
        model = Laptop_product
        fields = ['product_processor','product_ram','product_generation','product_storage','product_graphics','product_display']
        
