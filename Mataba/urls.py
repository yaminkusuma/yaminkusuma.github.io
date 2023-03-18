from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls.conf import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('tinymce/', include ('tinymce.urls')),
    path('', include('mywebsite.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# if settings.DEBUG:
#     urlpatterns 