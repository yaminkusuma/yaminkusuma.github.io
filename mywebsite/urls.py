from django.urls import path
from . import views

urlpatterns = [

    # login
    path('login/', views.login),

     # home
    # path('', views.home),
    # path('', views.bloghome, name='bloghome'),
    path('', views.jasahome, name='jasahome',),
    path('jasa/', views.jasa, name='jasa'),
    path('blog/', views.blog, name='blog'),
    path('about/', views.about),
    path('detailblog/<id>', views.detailblog, name='detailblog'),
    path('detailjasa/<id>', views.detailjasa, name='detailjasa'),
    path('sendwa/', views.sendwa, name='sendwa'),
    path('senddata/', views.senddata, name='senddata'),
    
    # Manajement CRUD Input data Jasa
    # path('', views.jasapage, name='inputjasa'),
    # path('add/', views.Addjasa, name='add'),
    # path('edit/', views.Edit, name='edit'),
    # path('update/<str:id>', views.Update, name='update'),
    # path('delete/<str:id>', views.Delete, name='delete'),

    # Manajement CRUD Input data Blog
    #  path('inputblog/', views.blogpage, name='inputblog'),
    #  path('addblog/', views.Addblog, name='addblog'),

    
]
