from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SomeModel(models.Model):
    name = models.CharField(max_length=100)

    def some_method(self):
        users = User.objects.all()  # Make sure this line is properly indented
