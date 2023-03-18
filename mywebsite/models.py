from PIL import Image
from django.db import models
from datetime import datetime, date

# from tinymce import models as tinymce_models


# Create your models here.


# class jasa
    # deskripsi = tinymce_models.HTMLField()
class Jasa(models.Model):
    nama = models.CharField(max_length=50, null=True)
    gambar = models.ImageField( upload_to='static/', default='static/artikel/mebel.jpg')
    judul = models.CharField(max_length=200, null=True, blank=True)
    deskripsi = models.TextField( blank=True)
    pembayaran = models.FloatField()
    datetime = models.DateTimeField(auto_now_add=True, null=True)
    pengerjaan = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.nama

# class blog
    # deskripsi = tinymce_models.HTMLField()
class Blog(models.Model):
    judul = models.CharField(max_length=200, null=True, blank=True)
    gambar = models.ImageField(upload_to='static/', default='static/artikel/mebel.jpg')
    nama = models.CharField(max_length=50, null=True)
    datetime = models.DateTimeField(auto_now_add=True, null=True)
    deskripsi = models.TextField( blank=True)
   

    def __str__(self):
        return self.nama