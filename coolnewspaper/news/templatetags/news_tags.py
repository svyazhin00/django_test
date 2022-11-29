from django import template
from news.models import *


register = template.Library()

@register.simple_tag(name = 'getcats')
def get_categories(filter = None):
    if filter == None:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk = filter)

@register.inclusion_tag('news/list_categories.html')
def show_categories(sort = None, cat_selected=0):
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)
    return {"cats": cats, 'cat_selected': cat_selected}


@register.inclusion_tag('news/list_menu.html')
def show_menu():

    menu = [{'title': 'Новости', 'url_name': 'about'},
            {'title': 'Календарь', 'url_name': 'dates'},
            {'title': 'Отзывы', 'url_name': 'reviews'}]

    return {"menu": menu}