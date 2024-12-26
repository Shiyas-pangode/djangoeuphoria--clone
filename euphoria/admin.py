from django.contrib import admin
from django.utils.html import format_html
from . models import TextUpload, ImageUpload ,ProductLoad ,Task




class TaskAdmin(admin.ModelAdmin):
    list_display = ('title','description','completed','created_at','updated_at')
admin.site.register (Task ,TaskAdmin)


class ImageUploadAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')

admin.site.register(ImageUpload , ImageUploadAdmin)


class productTextAdmin(admin.ModelAdmin):
    list_display = ('title',)
admin.site.register(TextUpload ,productTextAdmin)



class ProductthingAdmin(admin.ModelAdmin):
    list_display =('title','image',)

admin.site.register(ProductLoad ,ProductthingAdmin)

