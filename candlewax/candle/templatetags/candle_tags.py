from django import template

from candle.models import *

register = template.Library()


menu = [
    {'title': 'ИНФО', 'url_name': 'info'},
    {'title': 'О НАС', 'url_name': 'about'},
    {'title': 'ДОСТАВКА', 'url_name': 'delivery'},
    {'title': 'ОТЗЫВЫ', 'url_name': 'reviews'},
    {'title': 'ВОЙТИ', 'url_name': 'login'},
]
# @register.simple_tag(name='getmenu')
# def get_menu():
#     return menu

@register.inclusion_tag('candle/tags/list_menu.html')
def show_menu():
    return {"menu": menu}


# @register.simple_tag(name='cats')
# def get_categories(filter=None):
#     if not filter:
#         return Category.objects.all()
#     else:
#         return Category.objects.filter(pk=filter)

@register.inclusion_tag('candle/tags/list_categories.html')
def show_categories(sort=None, cat_selected=0):
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)

    return {"cats": cats, "cat_selected": cat_selected}