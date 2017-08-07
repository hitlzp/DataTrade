# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect,csrf_exempt
from news.models import news
# Create your views here.
def Addnews(request):
    return render_to_response("Addnews.html",context_instance=RequestContext(request))

@csrf_exempt
def savenews(request):
    title = request.POST.get('title')
    author = request.POST.get('author')
    date = request.POST.get('date')
    ttype = request.POST.get('type')
    content = request.POST.get('content')
    add = news(title = title,\
               author = author,
               date = date,\
               type = ttype,\
               content = content)
    add.save()
    return JsonResponse({"rr":1})

def main(request):
    add = []
    all_news = news.objects.filter(type = '市场新闻')
    print len(all_news)
    if len(all_news) > 4:
        for i in range(0, len(all_news)):
            if i> len(all_news) -5:
                add.append(all_news[len(all_news)-i -1])
    else:
        for i in range(0, len(all_news)):
            add.append(all_news[len(all_news)-i-1])
    content = {"mynews":add}
    return render_to_response("usermain.html",content,context_instance=RequestContext(request))

def news_detail(request):
    get = request.GET
    if get:
        thenews = news.objects.filter(id= get["id"])[0]
        content = {"thenews":thenews}
    return render_to_response("news.html",content,context_instance=RequestContext(request))
def news_list(request):
    Snews = news.objects.filter(type = '市场新闻')
    Hnews = news.objects.filter(type = '行业新闻')
    content = {"Snews":Snews,"Hnews":Hnews}
    return render_to_response("newslist.html",content,context_instance=RequestContext(request))