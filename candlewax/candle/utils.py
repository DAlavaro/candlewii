from .models import *


menu = [
    {'title': 'ИНФО', 'url_name': 'info'},
    {'title': 'О НАС', 'url_name': 'about'},
    {'title': 'ДОСТАВКА', 'url_name': 'delivery'},
    {'title': 'ОТЗЫВЫ', 'url_name': 'reviews'},
    {'title': 'ВОЙТИ', 'url_name': 'login'},
]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.all()

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(3)

        context['menu'] = user_menu
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0

        return context
