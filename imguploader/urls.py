
from django.contrib import admin
from django.urls import path, include

from image import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('image.urls')),
]
