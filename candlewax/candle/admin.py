from django.contrib import admin

from .models import Candle, Info, About, Delivery, Reviews, Category

class CandleAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'title',
                    'time_create',
                    'photo',
                    'is_published',
                    'price')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'price')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


admin.site.register(Candle, CandleAdmin)

admin.site.register(Category, CategoryAdmin)

admin.site.register(Info)

admin.site.register(About)

admin.site.register(Delivery)

admin.site.register(Reviews)
