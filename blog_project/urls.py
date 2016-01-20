# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

from blog.views import home
from blog_project import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', home, name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

