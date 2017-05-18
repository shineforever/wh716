#! coding:utf-8
"""wh716 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
import platform

from django.conf.urls import url
from django.contrib import admin
import xadmin
from django.views.static import serve

if platform.node() == 'guoletaodeMacBook-Pro.local':
    from wh716.settings.dev import MEDIA_ROOT
else:
    from wh716.settings.production import MEDIA_ROOT

from baoming.views import SearchView



urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    #配置用户上传文件后的url处理函数；
    url(r'^media/(?P<path>.*)$',serve,{'document_root':MEDIA_ROOT}),
    #身份证查询
    url(r'^search/$', SearchView.as_view(),name="search"),

    # url(r'^admin/', admin.site.urls),
]
