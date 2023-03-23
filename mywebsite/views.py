from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger #Untuk Pagination
from django import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect
from . import models

# login
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# models import
from .models import Jasa
from .models import Blog



# Create your views here.

# login
def login(req):
    return render(req, 'login/login.html')

# Home
def home(req):
    return render(req, 'home/home.html')

# def jasa(req):
def jasa(req):
    jasapage=Jasa.objects.all()
    context={   
        'jasapage':jasapage,
    }
    return render(req, 'home/jasa.html', context)

def jasahome(req):
    jasapage=Jasa.objects.all()
    blogpage=Blog.objects.all()

    # Pagination Product
    page = req.GET.get('page', 1)
    paginator = Paginator(blogpage, 3)
    try:
        blogpage = paginator.page(page)
    except PageNotAnInteger:
        blogpage = paginator.page(1)
    except EmptyPage:
        blogpage = paginator.page(paginator.num_pages)

    # page = req.GET.get('page', 1)
    # paginator = Paginator(jasapage, 1)
    # try:
    #     jasapage = paginator.page(page)
    # except PageNotAnInteger:
    #     jasapage = paginator.page(1)
    # except EmptyPage:
    #     jasapage = paginator.page(paginator.num_pages)

    context={
        'jasapage':jasapage,
        'blogpage':blogpage,
    }
    return render(req, 'home/home.html', context)



# def Blog(req):
def blog(req):
    blogpage=Blog.objects.all()
    context={      
        'blogpage':blogpage,
    }
    return render(req, 'home/blog.html', context)

def about(req):
    return render(req, 'home/about.html')

def sendwa(req):
    return render(req, 'home/sendwa.html')

def whatsappdata(Ph,Message):
    import time
    import webbrowser as web
    # import pyautogui as pg
    Phone = "+62"+Ph
    web.open('https://web.whatsapp.com/send?phone'+Phone+'&text='+Message)
    time.sleep(30)
    # web.press('enter')

def senddata(req):
    if req.method == 'POST':
        Ph = req.POST['Phone']
        Message = req.POST['Message']
        # print(Ph,Message)
        whatsappdata(Ph,Message)
        msg = "Sukses mengirim pesan..."
        return render(req, 'home/sendwa.html', {'msg':msg},)
    else:
        return HttpResponse("<h1>404 - Not Found :)</h1>")
   
def detailblog(req, id):
    blogpage = models.Blog.objects.filter(id=id).first()
    context={      
        'blogpage':blogpage,
    }
    return render(req, 'home/detailblog.html', context)

def detailjasa(req, id):
    jasapage = models.Jasa.objects.filter(id=id).first()
    context={      
        'jasapage':jasapage,
    }
    return render(req, 'home/detailjasa.html', context)

# Input Data Blog
# def blogpage(request):
#     return render(request, 'home/input_blog.html')

# def Addblog(request):
#     return render(request, 'home/input_blog.html')


# Input Data Jasa
# def jasapage(request):
#     jasapage=Jasa.objects.all()
#     context={
#         'jasapage':jasapage,
#     }
#     return render(request, 'home/input_jasa.html', context)

# def jasapage(request):
#     jasapage=Jasa.objects.all()
#     context={
#         'jasapage':jasapage,
#     }
#     return render(request, 'home/home.html', context)

# def Addjasa(request):
#     if request.method == "POST":
#         nama = request.POST.get('nama') 
#         gambar = request.POST.get('gambar') 
#         judul = request.POST.get('judul') 
#         deskripsi = request.POST.get('deskripsi')
#         pembayaran = request.POST.get('pembayaran')
#         pengerjaan = request.POST.get('pengerjaan') 

#         jasapage = Jasa(
#             nama = nama,
#             gambar = gambar,
#             judul = judul,
#             deskripsi = deskripsi,
#             pembayaran = pembayaran,
#             pengerjaan = pengerjaan,
#             )
#         jasapage.save()
#         return redirect('inputjasa')
#     return render(request, 'home/input_jasa.html')

# def Edit(request):
#     jasapage=Jasa.objects.all()
#     context={
#         'jasapage':jasapage,
#     }
#     return redirect(request, 'home/input_jasa', context)
    

# def Update(request, id):
#     if request.method == "POST":
#         nama = request.POST.get('nama')
#         gambar = request.POST.get('gambar')
#         judul = request.POST.get('judul')
#         deskripsi = request.POST.get('deskripsi')
#         pembayaran = request.POST.get('pembayaran')
#         pengerjaan = request.POST.get('pengerjaan')

#         jasapage=Jasa(
#             id = id,
#             nama = nama,
#             gambar = gambar,
#             judul = judul,
#             deskripsi = deskripsi,
#             pembayaran = pembayaran,
#             pengerjaan = pengerjaan,
#         )
#         jasapage.save()
#         return redirect('inputjasa')
#     return  redirect(request, 'home/input_jasa.html')

# def Delete(request, id):
#     jasapage=Jasa.objects.filter(id = id).delete()
#     context = {
#         'jasapage':jasapage,
#     }
#     return redirect('inputjasa')
    





