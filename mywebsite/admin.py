from django.contrib import admin
from .models import *

# Register your models here.

# admin.site.register(Jasa)

@admin.register(Jasa)
class JasaAdmin(admin.ModelAdmin):
    list_display = ['nama', 'judul', 'pembayaran', 'datetime']

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['judul', 'nama', 'datetime',]


# admin.site.register(Blog)
