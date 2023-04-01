from django.urls import path
from .views import *

urlpatterns = [
    path('', CandleHome.as_view(), name='home'),
    path('info/', CandleInfo.as_view(), name='info'),
    path('about/', CandleAbout.as_view(), name='about'),
    path('delivery/', CandleDelivery.as_view(), name='delivery'),
    path('reviews/', reviews, name='reviews'),
    path('login/', login, name='login'),
    path('buy/<int:buy_id>/', show_buy, name='buy'),
    path('catalog/<slug:cat_slug>', CandleCatalog.as_view(), name='catalog'),
    path('product/<slug:prod_slug>', ShowPost.as_view(), name='product'),
]