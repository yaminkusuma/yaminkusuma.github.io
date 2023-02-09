from django.urls import path
from . import views

urlpatterns = [

    # login
     path('login/', views.login),




    # home
    path('', views.home),

    path('jasa/', views.jasa),

    path('blog/', views.Blog),

    path('about/', views.about),

    path('detailblog/', views.detailblog),

]
