# -*- coding: utf-8 -*-
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
    url(r'^verification/$', emailverifi),  #邮箱验证
    url(r'^addnews/$', Addnews),   #添加新闻
    url(r'^Adminmain/$', Adminmain),   #管理员主界面
    url(r'^Admin_User_Search/$', Adminusersearch),  #管理员用户信息查询
    url(r'^Admin_Edit_User/$', Adminuseredit),  #管理员编辑用户信息
    url(r'^savenews/$', savenews),   #写新闻
    url(r'^main/$', main),   #主界面
    url(r'^news_detail/$', news_detail),   #展示新闻
    url(r'^news_list/$', news_list),   #新闻中心，展示新闻列表
    url(r'^phomepage/$', phomepage),  #个人主界面
    url(r'^mymess/$', mymess),    #?
    url(r'^about/$', about),  #?
    url(r'^data/$', data),   #?
    url(r'^data/select/$', data_sel),   #? 
    url(r'^data/bargain/$', data_bargain),   #?
    url(r'^data_detail/$', data_detail),  #?
    #uEditor ---start   百度编辑器插件
    url(r'ueEditorControler','news.controller.handler'),
    url( r'^UE/(?P<path>.*)$', 'django.views.static.serve',{ 'document_root': (ROOT+"/UE").replace('\\','/')}),
    url( r'^upload/(?P<path>.*)$', 'django.views.static.serve',{ 'document_root': (ROOT+"/upload").replace('\\','/') }),
    #uEditor ---end
    
    url(r'^uploaddata/$', uploaddata),   #上传数据  发布数据
    url(r"^check_existing/$",check_existing),  #插件
    url(r"^upload_image/$",upload_image),   #只起调用函数作用
    url(r"^mydata/$",mydata),    #已发布数据
    url(r"^mydata/bargain/$",mydata_bargain),     #已发布议价数据
    url(r"^data/bargain/select/$",data_bargain_sel),     #已发布议价数据(加标签) 
    
    url(r'^check_data_list/$', check_data_list),
    url(r'^check_data_detail/$', check_data_detail),
    
    url(r'^data/buydata/$', buydt), 
    url(r'^data/set/$', buyset),

    url(r'^bought_data_list/$', bought_data_list),
    
    url(r'^fixed_price_s/$', fixedPrice_sell),
    url(r'^fixed_price_b/$', fixedPrice_buy), 
    
    url(r'^publish/bargain/$', uploaddata_baigain),  #发布议价数据 
    url(r"^upload_image_bargain/$",upload_image_bargain),   #只起调用函数作用
<<<<<<< HEAD

    url(r'^fixed_price_list/$', fixed_price_list), #展示用户议价订单，包括买和卖
    url(r'^fixed_price_detail/$', fixed_price_detail), #展示用户议价订单，包括买和卖
=======
>>>>>>> hitlzp/master
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
