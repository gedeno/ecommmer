from django.db import models

# Create your models here.
class Normal_product(models.Model):
    product_brand = models.CharField(max_length=200)
    product_name = models.CharField(max_length=100)
    product_price = models.IntegerField()
    product_image = models.ImageField(upload_to='photos/')
    def __str__(self):
        return self.product_name
class Phone_product(models.Model):
    product_display = models.IntegerField()
    product_camera = models.CharField(max_length=100)
    product_battery = models.CharField(max_length=200)
    product_ram = models.CharField(max_length=200)
    product_storage = models.CharField(max_length=200)
    all_info = models.ForeignKey(Normal_product,on_delete=models.CASCADE)
    def __str__(self):
        return self.all_info.product_name
class Laptop_product(models.Model):
    product_processor = models.CharField(max_length=200)
    product_ram = models.CharField(max_length=200)
    product_generation = models.CharField(max_length=200)
    product_storage = models.CharField(max_length=200)
    product_graphics = models.CharField(max_length=200)
    product_display = models.CharField(max_length=200)
    all_info = models.ForeignKey(Normal_product,on_delete=models.CASCADE)
    def __str__(self):
        return self.all_info.product_name



