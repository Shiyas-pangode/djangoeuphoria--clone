from django.contrib import admin
from  .models import ImageUpload
from django.utils.html import format_html

admin.site.register(ImageUpload)
class ImageUploadAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')

    