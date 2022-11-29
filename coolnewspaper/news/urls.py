from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index, name = 'home'),
    path('about/', about, name = 'about'),
    path('dates/', dates, name = 'dates'),
    path('reviews/', reviews, name = 'reviews'),
    path('post/<slug:post_slug>/', show_post, name = 'post'),
    path('cat/<slug:cat_slug>/', show_category, name = 'category')


]