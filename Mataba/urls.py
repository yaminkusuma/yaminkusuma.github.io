
from django.contrib import admin
from django.urls.conf import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mywebsite.urls')),
]
