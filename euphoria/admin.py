from django.contrib import admin
from  .models import ImageUpload
from django.utils.html import format_html
from .models import TextUpload
from . models import ProductLoad

admin.site.register(ImageUpload)
class ImageUploadAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')



admin.site.register(TextUpload)
class productTextAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(ProductLoad)
class ProductthingAdmin(admin.ModelAdmin):
    list_display =('name','image')