#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response,HttpResponse
from account.Helper import Checkcode
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
import StringIO
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

import smtplib  #加载smtplib模块
from email.mime.text import MIMEText
from email.utils import formataddr
import datetime

my_sender='15754603160@163.com' #发件人邮箱账号，为了后面易于维护，所以写成了变量
emailurl = '127.0.0.1:8000/verification?'

@csrf_protect
def login(request):
    content = ''
    if request.user.id:
        return HttpResponseRedirect("/main/")
    if request.POST:
        post = request.POST
        email = post["email"]
        password = post["password"]
        user = auth.authenticate(username=email, password=password)
        if (user is not None):
            if user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect("/main/")
            else:
                content = '用户尚未激活，请去邮箱激活'
        else:
            content = '账号或密码错误'
    return render_to_response("login.html",{'error':content},context_instance=RequestContext(request))

@csrf_protect
def register(request):
    content = ''
    if request.user.id:
        return HttpResponseRedirect("/main/")
    if request.POST:
        post = request.POST
        username = post["user"]
        password = post["password"]
        email = post["email"]
        if username and password and email:
            if not User.objects.filter(username = email):
                new_user = User.objects.create_user( \
                                            username = email, \
                                            password = password, \
                                            first_name = username, \
                                           )
                new_user.save()
                User.objects.filter(username = email).update(is_active = 0)
                user = auth.authenticate(username=email, password=password)
                if (user is not None):
                    if user.is_active:
                        auth.login(request, user)
                        return HttpResponseRedirect("/main/")
                    else:
                        content = '激活信息已发送至邮箱，请于24小时内完成激活'
                        mystr = 'username='+str(email)
                        my_user = str(email)
                        ret = mail(request, emailurl+mystr, my_user)
                        if ret:
                            print("ok") #如果发送成功则会返回ok，稍等20秒左右就可以收到邮件
                        else:
                            print("filed")  #如果发送失败则会返回filed

            else:
                if User.objects.filter(username = email)[0].is_active == 0:#用户注册过但未激活
                    User.objects.filter(username = email).delete()
                    new_user = User.objects.create_user( \
                                            username = email, \
                                            password = password, \
                                            first_name = username, \
                                           )
                    new_user.save()
                    User.objects.filter(username = email).update(is_active = 0)
                    mystr = 'username='+str(email)
                    my_user = str(email)
                    ret = mail(request, emailurl+mystr, my_user)
                    if ret:
                        print("ok") #如果发送成功则会返回ok，稍等20秒左右就可以收到邮件
                    else:
                        print("filed")  #如果发送失败则会返回filed
                    content = '激活信息已发送至邮箱，请于24小时内完成激活'
                else:    #用户注册且激活成功
                    content = '用户已存在，请直接登陆'
    return render_to_response("register.html",{'error':content},context_instance=RequestContext(request))

def logout(request):#注销
    auth.logout(request)
    return HttpResponseRedirect("/main/")

def mail(request, url, my_user):#发邮件
    ret=True
    content = "点击或复制以下链接到浏览器中以完成验证："+url
    try:
        msg=MIMEText(content,'plain','utf-8')
        msg['From']=formataddr(["哈工大大数据",my_sender])   #括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To']=formataddr(["",my_user])   #括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject']="哈工大大数据" #邮件的主题，也可以说是标题

        server=smtplib.SMTP("smtp.163.com",25)  #发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender,"24861937")    #括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender,[my_user,],msg.as_string())   #括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()   #这句是关闭连接的意思
    except Exception:   #如果try中的语句没有执行，则会执行下面的ret=False
        ret=False
    return ret

def emailverifi(request):#验证邮箱
    username = request.GET['username']
    
    now = datetime.datetime.now()
    date = now + datetime.timedelta(days = -1)
    theuser = User.objects.filter(username = username)
    if theuser:
        if str(theuser[0].date_joined) > str(date):
            User.objects.filter(username = username).update(is_active = 1)
            return HttpResponseRedirect("/main/")

def CheckCode(request):
    mstream = StringIO.StringIO()
    validate_code = Checkcode.create_validate_code()
    img = validate_code[0] 
    img.save(mstream, "GIF")
    
    #将验证码保存到session
    request.session["CheckCode"] = validate_code[1]
    
    return HttpResponse(mstream.getvalue()) 


def Login(request):
    print request.method
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pwd')
        check_code = request.POST.get('checkcode')
        #从session中获取验证码
        session_code = request.session["CheckCode"]
        if check_code.strip().lower() != session_code.lower():
            return HttpResponse('验证码不匹配')
        else:
            return HttpResponse('验证码正确')          
        
    return render_to_response('login2.html',{'error':"",'username':'','pwd':'' })


