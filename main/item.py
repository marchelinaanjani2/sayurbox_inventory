from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    date_added = models.DateField(auto_now_add=True)
    price = models.IntegerField()
    amount = models.IntegerField()
    description = models.TextField() 
    stock = models.IntegerField(default=0)  

    image = models.ImageField(upload_to='product_images/', default='default_image.jpg') 

    def __str__(self):
        return self.name
