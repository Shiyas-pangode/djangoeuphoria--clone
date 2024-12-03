from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns=[
    path('',views.index,name='index'),
    path('about/',views.shiyas,name='shiyas'),
    path('cart/',views.cart, name = 'cart'),
    path('products/',views.products, name = 'products')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)