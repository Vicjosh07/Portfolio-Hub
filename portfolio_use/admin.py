from django.contrib import admin
from .models import *
# Register your models here.

class BlogsAdmin(admin.ModelAdmin):
    list_display=(
    'title',
    'description',
    'authname',)
    search_fields = ('title','authname')
    list_filter = ['title']
admin.site.register(Blogs, BlogsAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display=(
    'name',
    'email',
    'phonenumber',
    'description',)
    search_fields = ('name','email')
admin.site.register(Contact, ContactAdmin)