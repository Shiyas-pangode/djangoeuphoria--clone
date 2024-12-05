from django.shortcuts import render
from django.http import HttpResponse
from  .models import ImageUpload
from .models import TextUpload

def index(request):
    return render(request ,"index.html")

def shiyas(request):
    return HttpResponse("hiiii")

def cart(request):
    return render(request , "cart.html")

def products(request):
    return render(request, "product.html")

def imagelist(request):
    images = ImageUpload.objects.all()
    return render(request, "index.html" ,{'images' : ImageUpload} )

def productlist(request):
    title = TextUpload.object.all()
    return render(request,"product.html" ,{'title' :title})

def productext(request):
    title = TextUpload.objects.all()
    print(title)
    return render(request,"product.html" ,{'title' :title})
    