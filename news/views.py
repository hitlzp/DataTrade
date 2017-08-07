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