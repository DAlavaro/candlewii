from django import template

from candle.models import Category

register = template.Library()


@register.simple_tag(name='cats')
def get_categories(filter=None):
    if not filter:
        return Category.objects.all()
    else: return Category.ibjects.filter(pk=filter)

@register.inclusion_tag('candle/list_categories.html')
def show_categories():
    cats = Category.objects.all()
    return {"cats": cats}