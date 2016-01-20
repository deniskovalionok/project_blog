# -*- coding: utf-8 -*-
from django.conf.urls import url, patterns

from blog.views import about, article

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^about/$', about, name='about'),
    url(r'^(?P<slug>[-\w]+)$', article, name='article')
)
