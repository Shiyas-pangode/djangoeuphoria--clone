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
                



