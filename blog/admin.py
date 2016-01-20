# -*- coding: utf-8 -*-
from django.contrib import admin
from blog.models import Article

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'time')


admin.site.register(Article, ArticleAdmin)