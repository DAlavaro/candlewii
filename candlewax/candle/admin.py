from django.contrib import admin

from .models import Candle, Info, About, Delivery, Reviews

admin.site.register(Candle)

admin.site.register(Info)

admin.site.register(About)

admin.site.register(Delivery)

admin.site.register(Reviews)
