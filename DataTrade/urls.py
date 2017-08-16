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

from account.views import *
from news.views import *
from data.views import *

from django.conf.urls.static import static
from django.conf import settings
import os
ROOT = os.path.dirname(__file__)

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
    url(r'^main/$', main),
    url(r'^news_detail/$', news_detail),
    url(r'^news_list/$', news_list),
    url(r'^phomepage/$', phomepage),
    url(r'^mymess/$', mymess),
    url(r'^about/$', about),
    url(r'^data/$', data),
    url(r'^data_detail/$', data_detail),
    #uEditor ---start
    url(r'ueEditorControler','news.controller.handler'),
    url( r'^UE/(?P<path>.*)$', 'django.views.static.serve',{ 'document_root': (ROOT+"/UE").replace('\\','/')}),
    url( r'^upload/(?P<path>.*)$', 'django.views.static.serve',{ 'document_root': (ROOT+"/upload").replace('\\','/') }),
    #uEditor ---end
    
    url(r'^uploaddata/$', uploaddata),
    url(r"^check_existing/$",check_existing), 
    url(r"^upload_image/$",upload_image), 
    url(r"^mydata/$",mydata), 
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
