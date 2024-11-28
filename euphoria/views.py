from django.shortcuts import render
from django.http import HttpResponse
from  .models import ImageUpload

def index(request):
    return render(request ,"index.html")

def shiyas(request):
    return HttpResponse("hiiii")

def imagelist(request):
    images = ImageUpload.objects.all()
    return render(request, "index.html" ,{'images' : ImageUpload} )