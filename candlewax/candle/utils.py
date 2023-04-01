from candle.models import *

menu = [
    {'title': 'ИНФО', 'url_name': 'info'},
    {'title': 'О НАС', 'url_name': 'about'},
    {'title': 'ДОСТАВКА', 'url_name': 'delivery'},
    {'title': 'ОТЗЫВЫ', 'url_name': 'reviews'},
    {'title': 'ВОЙТИ', 'url_name': 'login'},
]


class DaraMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Catego*ry.objects.all()
        context['menu'] = menu
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context
