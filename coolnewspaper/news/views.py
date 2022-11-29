from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404

from .models import *



def index(request):
    posts = Newspaper.objects.all()
    
    context = {
        'posts': posts,
        'title': 'Главная страница',
        'cat_selected': 0
    }

    return render(request,'news/index.html', context = context)

def about(request):
    return render(request,'news/about.html', {'title': 'О портале'})

def dates(request):
    return HttpResponse('Я календарь, переверну...')

def reviews(request):
    return HttpResponse('Доллар - грязная, никчемная бумажка')



def show_post(request, post_slug):
    post = get_object_or_404(Newspaper, slug=post_slug)

    context = {
        'post': post,
        #'menu': menu,
        'title': 'Главная страница',
        'cat_selected': post.cat_id
    }
    return render(request, 'news/post.html', context=context)



def show_category(request, cat_slug):
    posts = Newspaper.objects.filter(cat__slug = cat_slug)


    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        #'menu': menu,
        'title': 'Отображение по категориям',
        'cat_selected':  cat_slug
    }

    return render(request, 'news/index.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound(f'страница не найдена по префиксу')



