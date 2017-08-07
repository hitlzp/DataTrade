"""DataTrade URL Configuration

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
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

from account.views import login,register,logout,emailverifi,Adminmain,Adminusersearch,Adminuseredit  
from news.views import Addnews,savenews

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', login),
    url(r'^register/$', register),
    url(r'^logout/$', logout),
    url(r'^verification/$', emailverifi),
    url(r'^addnews/$', Addnews),
    url(r'^Adminmain/$', Adminmain),
    url(r'^Admin_User_Search/$', Adminusersearch),
    url(r'^Admin_Edit_User/$', Adminuseredit),
    url(r'^savenews/$', savenews),
    
]
