from django.contrib import admin
from django.urls import path, include

from candle.views import pageNotFound

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('candle.urls')),
]

handler404 = pageNotFound
