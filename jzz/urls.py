from django.conf.urls import patterns, include, url
from blog.views import *
from blog.models import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'jzz.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^blog/', include('blog.urls')),
    ('^index/$', index),
    ('^hello/$', hello),
    ('^blog/$', blog),
    ('^writeblog/$', writeblog),
    (r'^wbsub/$', wbsub),
    (r'^ArticleShow/$', ArticleShow),
    #('^index/$', index) 
    #url(r'^admin/', include(admin.site.urls)),
)
