from django.urls import path
from .views import index, info, reviews

urlpatterns = [
    path('', index, name='home'),
    path('info/', info, name='info')
]

