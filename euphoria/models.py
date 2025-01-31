from django.db import models
from django.contrib.auth.models import User
from django.db import models



class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class ImageUpload(models.Model):
    title = models.CharField(max_length=100)  # Example field
    image = models.ImageField(upload_to='images/')  # Field for image upload

    def __str__(self):
        return self.title

        
class TextUpload(models.Model):
    title = models.CharField(max_length = 100)

    def __str__(self):
        return self.title

class ProductLoad(models.Model):
    title = models.CharField(max_length=255, default="Default Title")
    image = models.ImageField(upload_to = 'images/')


    def __str__(self):
        return self.title
                

class product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=400)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"


