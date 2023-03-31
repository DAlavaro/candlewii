from django.urls import path
from .views import *

urlpatterns = [
    path('', CandleHome.as_view(), name='home'),
    path('info/', info, name='info'),
    path('about/', about, name='about'),
    path('delivery/', delivery, name='delivery'),
    path('reviews/', reviews, name='reviews'),
    path('login/', login, name='login'),
    path('buy/<int:buy_id>/', show_buy, name='buy'),
    path('catalog/<slug:cat_slug>', CandleCatalog.as_view(), name='catalog'),
    path('product/<slug:prod_slug>', ShowPost.as_view(), name='product'),
]