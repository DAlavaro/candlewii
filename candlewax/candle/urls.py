from django.urls import path
from .views import index, info, about, delivery, reviews, login, show_buy, show_catalog

urlpatterns = [
    path('', index, name='home'),
    path('info/', info, name='info'),
    path('about/', about, name='about'),
    path('delivery/', delivery, name='delivery'),
    path('reviews/', reviews, name='reviews'),
    path('login/', login, name='login'),
    path('buy/<int:buy_id>/', show_buy, name='buy'),
    path('catalog/<int:cat_id>', show_catalog, name='catalog')

]