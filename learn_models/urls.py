# -*- coding: UTF-8 -*-
"""learn_models URL Configuration

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

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/','learn.views.hello',name='hello'),
    url(r'^test/','learn.views.test',name='test'),
    
    # url(r'^myhtml/$',myhtml),  
    # url(r'^cc/$',bb),  
    #url映射到view层，并获取展现数据  
    url(r'^show$','learn.views.show',name='show'),
    #批量删除所选条目  
    url(r'^delSelect$','learn.views.delSelect',name='delSelect'),
    #查询所有数据的映射  
    url(r'^q$','learn.views.query',name='query'),  
    #查询所有数据的映射  
    url(r'^query$','learn.views.queryById',name='queryById'), 
    #添加数据映射  
    url(r'^add$','learn.views.add',name='add'),  
    #访问添加首页的html  
    url(r'^index.html$','learn.views.beginAdd',name='beginAdd'),  
    #删除用户根据id  
    url(r'delete$','learn.views.delByID',name='delByID'),  
    #更新的方法，根据id  
    url(r'showid$','learn.views.showUid',name='showUid'),

]
