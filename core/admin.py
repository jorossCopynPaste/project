from django.contrib import admin

# Register your models here.
from .models import publicPhoto, publicCategory

admin.site.register(publicCategory)
admin.site.register(publicPhoto)