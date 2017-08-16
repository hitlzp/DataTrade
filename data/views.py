# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from data.models import alldata,datastate
from django.contrib.auth.models import User
import datetime
# Create your views here.

@csrf_exempt
def check_existing(request):
    return HttpResponse('0')

def uploaddata(request):
    userid =  request.user.id
    thisuser = User.objects.filter(id = userid)[0]
    post = request.POST
    text =''
    if post:
        if request.FILES.get('img'):
            undone = alldata.objects.filter(isaval=0, owner_id = userid)
            if undone:
                fname = undone[len(undone)-1].file_name
                fscale = undone[len(undone)-1].file_scale
                ffile = undone[len(undone)-1].file
                fdemo = undone[len(undone)-1].Show_demo
                now = datetime.datetime.now()
                add = alldata(
                            file_name = fname,
                            file_scale = fscale,
                            file = ffile,
                            Show_demo = fdemo,
                            owner_id = userid,
                            picture = request.FILES.get('img'),
                            isaval = 1,
                            post_time = now,
                            exchange  = int(post['sel1']),
                            introduce = post['message'],
                            price = post['price'],
                            limit = int(post['sel2']),
                            limit_count = post['usersum'],
                            type = int(post['sel3']),
                            dataname = post['dataname']
                            )
                add.save()
                alldata.objects.filter(owner_id = userid, isaval = 0).delete()
                
                add2 = datastate(
                                 dataid_id = add.id,
                                 owner_id = userid,
                                 state = 0
                                 )
                add2.save()
                return HttpResponseRedirect("/mydata/")
            else:
                text = "请上传文件"
        else:
            text = "请上传图片"
    content= {"text":text,"thisuser":thisuser}
    return render_to_response("publish.html",content,context_instance=RequestContext(request))

@csrf_exempt
def upload_image(request):
    userid =  request.user.id
    reqfile = request.FILES['Filedata']
    thetype = request.POST.get('thetype')
    if (reqfile.size / 1024) > (1024 *1024):
        thesize = str(round(reqfile.size / (1024.0 * 1024.0 *1024.0),2)) + 'G'
    elif (reqfile.size / 1024) > 1024:
        thesize = str(round(reqfile.size / (1024.0 * 1024.0),2)) + 'MB'
    else:
        thesize = str(round(reqfile.size / 1024.0,2)) + 'KB'
    print thesize
    undone = alldata.objects.filter(isaval=0, owner_id = userid)
    if undone:
        if int(thetype) == 1:
            sdemo = undone[len(undone)-1].Show_demo
            add = alldata(
                          file_name = reqfile.name,
                          file_scale = thesize,
                          file = reqfile,
                          owner_id = userid,
                          isaval = 0,
                          Show_demo = sdemo
                          )
            add.save()
            alldata.objects.filter(id = undone[len(undone)-1].id).delete()
        else:
            fname = undone[len(undone)-1].file_name
            fscale = undone[len(undone)-1].file_scale
            ffile = undone[len(undone)-1].file
            add = alldata(
                          file_name = fname,
                          file_scale = fscale,
                          file = ffile,
                          Show_demo = reqfile,
                          owner_id = userid,
                          isaval = 0
                          )
            add.save()
            alldata.objects.filter(id = undone[len(undone)-1].id).delete()
            
    else:
        if int(thetype) == 1:
            add = alldata(
                          file_name = reqfile.name,
                          file_scale = thesize,
                          file = reqfile,
                          owner_id = userid,
                          isaval = 0
                          )
            add.save()
        else:
            add = alldata(
                          Show_demo = reqfile,
                          owner_id = userid,
                          isaval = 0
                          )
            add.save()
    return HttpResponse(1)

def mydata(request):
    temp = []#已发布数据
    temp2 = []#审核中数据
    temp3 = [] #未通过数据
    userid =  request.user.id
    thisuser = User.objects.filter(id = userid)[0]
    datas = datastate.objects.filter(owner_id = request.user.id, state = 1)
    for d in datas:
        temp.append(alldata.objects.get(owner_id = request.user.id, id = d.dataid_id))
        
    datas = datastate.objects.filter(owner_id = request.user.id, state = 0)
    for d in datas:
        temp2.append(alldata.objects.get(owner_id = request.user.id, id = d.dataid_id))
        
    datas = datastate.objects.filter(owner_id = request.user.id, state = -1)
    for d in datas:
        rr = []
        tt = alldata.objects.get(owner_id = request.user.id, id = d.dataid_id)
        rr.append(tt.id)
        rr.append(tt.dataname)
        rr.append(d.detail)
        temp3.append(rr)
    
    content = {'mydata':temp,'mydata2':temp2,'mydata3':temp3,"thisuser":thisuser}
    return render_to_response("mydata.html",content,context_instance=RequestContext(request))
    