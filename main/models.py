from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    date_added = models.DateField(auto_now_add=True)
    price = models.IntegerField()
    amount = models.IntegerField()
    description = models.TextField() 
    stock = models.IntegerField(default=0)  

    image = models.ImageField(upload_to='product_images/', default='default_image.jpg') 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
# class Employee(models.Model):
#     nama = models.CharField(max_length=255)
#     umur = models.IntegerField()

#     def __str__(self):
#         return self.name
