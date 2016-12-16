"""ec_report URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from ec_report import settings
import os

urlpatterns = [
    url(r'^images/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': os.path.join(settings.STATIC_PATH, 'images')}),
    url(r'^$', 'report_show.views.index'),
    url(r'^state/$', 'report_show.views.state'),
    url(r'^style/$', 'report_show.views.style'),
    url(r'^team/$', 'report_show.views.team'),
    url(r'^upload/$', 'upload.views.upload', name='upload'),
    url(r'^admin/', include(admin.site.urls)),
]
