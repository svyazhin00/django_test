from django.contrib import admin
from .models import *

class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}

class CotegoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_list = ('id','name')
    search_fields = ('name',)
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Newspaper, CourseAdmin)
admin.site.register(Category, CotegoryAdmin)
