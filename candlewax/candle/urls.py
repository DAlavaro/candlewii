from django.urls import path
from .views import index, info, reviews

urlpatterns = [
    path('', index),
    path('info/', info),
    path('reviews/<int:idr>', reviews),
]

