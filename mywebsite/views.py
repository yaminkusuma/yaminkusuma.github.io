from django.shortcuts import render

from django import forms
from django.shortcuts import render, redirect
from . import models

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User


# Create your views here.


# login
def login(req):
    return render(req, 'login/login.html')



# Home
def home(req):
    return render(req, 'home/home.html')

def jasa(req):
    return render(req, 'home/jasa.html')

def Blog(req):
    return render(req, 'home/blog.html')

def about(req):
    return render(req, 'home/about.html')

def detailblog(req):
    return render(req, 'home/detailblog.html')
