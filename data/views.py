# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from data.models import alldata,datastate,buydata,alldata_bargain,datastate_bargain
from django.contrib.auth.models import User
import datetime
from django.http import JsonResponse
from random import randint
# Create your views here.

@csrf_exempt
def check_existing(request):
    return HttpResponse('0')

def uploaddata(request):
    userid =  request.user.id
    thisuser = User.objects.filter(id = userid)[0]
    url = 'img/pic_url_' + str(randint(1,4)) + '.png'
    print url
    post = request.POST
    if post:
            undone = alldata.objects.filter(isaval=0, owner_id = userid)
            dataid = undone[len(undone)-1]
            now = datetime.datetime.now()
            if undone:
                alldata.objects.filter(isaval=0, owner_id = userid).update(
                            owner_id = userid,
                            picture = url,
                            isaval = 1,
                            exchange  = int(post['sel1']),
                            introduce = post['message'],
                            price = post['price'],
                            limit = int(post['sel2']),
                            limit_count = post['usersum'],
                            type = int(post['sel3']),
                            post_time = now,
                            dataname = post['dataname']
                            )
                alldata.objects.filter(owner_id = userid, isaval = 0).delete()
                add = datastate(
                                 dataid = dataid,
                                 owner_id = userid,
                                 state = 0
                                 )
                add.save()
                return HttpResponseRedirect("/mydata/")
    content= {"thisuser":thisuser}
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
        try:
            temp.append(alldata.objects.get(owner_id = request.user.id, id = d.dataid_id))
        except:
            print 111
        
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

def mydata_bargain(request):
    temp = []#已发布数据
    temp2 = []#审核中数据
    temp3 = [] #未通过数据
    userid =  request.user.id
    thisuser = User.objects.filter(id = userid)[0]
    datas = datastate_bargain.objects.filter(owner_id = request.user.id, state = 1)
    for d in datas:
        temp.append(alldata_bargain.objects.get(owner_id = request.user.id, id = d.dataid_id))
        
    datas = datastate_bargain.objects.filter(owner_id = request.user.id, state = 0)
    for d in datas:
        temp2.append(alldata_bargain.objects.get(owner_id = request.user.id, id = d.dataid_id))
        
    datas = datastate_bargain.objects.filter(owner_id = request.user.id, state = -1)
    for d in datas:
        rr = []
        tt = alldata_bargain.objects.get(owner_id = request.user.id, id = d.dataid_id)
        rr.append(tt.id)
        rr.append(tt.dataname)
        rr.append(d.detail)
        temp3.append(rr)
    
    content = {'mydata':temp,'mydata2':temp2,'mydata3':temp3,"thisuser":thisuser}
    return render_to_response("mydata_bargain.html",content,context_instance=RequestContext(request))

    
#author sctian
def check_data_list(request):
    userid = request.user.id
    thisuser = User.objects.filter(id = userid)[0]
    datas = datastate.objects.all()
    content = {'data_list' : datas}
    return render_to_response("check_data_list.html", content, context_instance=RequestContext(request))

#author sctian
def check_data_detail(request):
    admin_id = request.user.id
    admin_name = User.objects.filter(id = admin_id)[0].username
    get = request.GET
    data = datastate.objects.get(dataid_id = get["dataid"])
    post = request.POST
    if post:
        if post['feedback'] != '':
            data.detail = post['feedback']
            data.save()
        if post['judge'] == 'yes':
            data.state = 1
            data.save()
        if post['judge'] == 'no':
            data.state = -1
            data.save()
    content = {'data': data}
    return render_to_response("check_data_detail.html",content,context_instance=RequestContext(request))
def data(request):
    data0=datastate.objects.filter(state = 1)
    data1=[]
    for i in data0:
        if not i.owner_id  == request.user.id:
            data1.append(alldata.objects.get(id=i.dataid_id))
    content={}
    content['data']=data1
    content['css']= 0
    return render_to_response("data.html",content,context_instance=RequestContext(request))

def data_sel(request):
    data0=datastate.objects.filter(state = 1)
    data1=[]
    tag = request.GET['tag']
    for i in data0:
        if not i.owner_id  == request.user.id:
            if int(tag) == 0:
                data1.append(alldata.objects.get(id=i.dataid_id))
            else:
                try:
                    data1.append(alldata.objects.get(id=i.dataid_id,type=str(tag)))
                except:
                    print str(tag)
    content={}
    content['data']=data1
    content['css']= int(tag)
    return render_to_response("data.html",content,context_instance=RequestContext(request))

def data_bargain(request):
    data0=datastate_bargain.objects.filter(state = 1)
    data1=[]
    for i in data0:
        if not i.owner_id  == request.user.id:
            data1.append(alldata_bargain.objects.get(id=i.dataid_id))
    content={}
    content['data']=data1
    content['css']= 0
    return render_to_response("data_bargain.html",content,context_instance=RequestContext(request))

def data_bargain_sel(request):
    tag = request.GET['tag']
    data0=datastate_bargain.objects.filter(state = 1)
    data1=[]
    for i in data0:
        if not i.owner_id  == request.user.id:
            if int(tag) == 0:
                data1.append(alldata_bargain.objects.get(id=i.dataid_id))
            else: 
                try:
                    data1.append(alldata_bargain.objects.get(id=i.dataid_id,type=str(tag)))
                except:
                    print str(tag)
    
    content={}
    content['data']=data1
    content['css']= int(tag)
    return render_to_response("data_bargain.html",content,context_instance=RequestContext(request))

def data_detail(request):
    get = request.GET
    data = alldata.objects.get(id = get["id"])
    content={}
    content['data']=data
    if buydata.objects.filter(buyer_id = request.user.id, data_id = data):
        set = 1
    else:
        set = 0
    content['set']=set
    return render_to_response("data_detail.html",content,context_instance=RequestContext(request))

@csrf_exempt
def buydt(request):
    dataid = request.POST.get('dataid')
    userid =  request.user.id
    now = datetime.datetime.now()
    thedata = alldata.objects.get(id = dataid)
    
    add = buydata(
                  post_time = now,
                  price = thedata.price,
                  buyer_id = userid,
                  data = thedata,
                  )
    add.save()
    return JsonResponse({"rr":dataid})

@csrf_exempt
def buyset(request):
    temp = []
    alld = buydata.objects.filter(buyer_id = request.user.id)
    for d in alld:
        temp.append(int(d.data_id))
    return JsonResponse({"rr":temp,'length':len(temp)})
#author sctian
def bought_data_list(request):
    userid = request.user.id
    try:
        datas = buydata.objects.filter(buyer = userid)
        name = User.objects.get(id = userid)
        content = {'data_list': datas,'thisuser':name}

    except:
        content = {}
    return render_to_response("bought_data_list.html", content, context_instance=RequestContext(request))

def uploaddata_baigain(request):
    userid =  request.user.id
    thisuser = User.objects.filter(id = userid)[0]
    url = 'img/pic_url_' + str(randint(1,4)) + '.png'
    print url
    post = request.POST
    if post:
            undone = alldata_bargain.objects.filter(isaval=0, owner_id = userid)
            dataid = undone[len(undone)-1]
            now = datetime.datetime.now()
            if undone:
                alldata_bargain.objects.filter(isaval=0, owner_id = userid).update(
                            owner_id = userid,
                            picture = url,
                            isaval = 1,
                            exchange  = int(post['sel1']),
                            introduce = post['message'],
                            price = post['price'],
                            limit = int(post['sel2']),
                            limit_count = post['usersum'],
                            type = int(post['sel3']),
                            post_time = now,
                            dataname = post['dataname']
                            )
                alldata_bargain.objects.filter(owner_id = userid, isaval = 0).delete()
                add = datastate_bargain(
                                 dataid = dataid,
                                 owner_id = userid,
                                 state = 0
                                 )
                add.save()
                return HttpResponseRedirect("/mydata/")
    content= {"thisuser":thisuser}
    return render_to_response("publish_bargain.html",content,context_instance=RequestContext(request))
<<<<<<< HEAD


@csrf_exempt
def upload_image_bargain(request):
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
    undone = alldata_bargain.objects.filter(isaval=0, owner_id = userid)
    if undone:
        if int(thetype) == 1:
            sdemo = undone[len(undone)-1].Show_demo
            add = alldata_bargain(
                          file_name = reqfile.name,
                          file_scale = thesize,
                          file = reqfile,
                          owner_id = userid,
                          isaval = 0,
                          Show_demo = sdemo
                          )
            add.save()
            alldata_bargain.objects.filter(id = undone[len(undone)-1].id).delete()
        else:
            fname = undone[len(undone)-1].file_name
            fscale = undone[len(undone)-1].file_scale
            ffile = undone[len(undone)-1].file
            add = alldata_bargain(
                          file_name = fname,
                          file_scale = fscale,
                          file = ffile,
                          Show_demo = reqfile,
                          owner_id = userid,
                          isaval = 0
                          )
            add.save()
            alldata_bargain.objects.filter(id = undone[len(undone)-1].id).delete()
            
    else:
        if int(thetype) == 1:
            add = alldata_bargain(
                          file_name = reqfile.name,
                          file_scale = thesize,
                          file = reqfile,
                          owner_id = userid,
                          isaval = 0
                          )
            add.save()
        else:
            add = alldata_bargain(
                          Show_demo = reqfile,
                          owner_id = userid,
                          isaval = 0
                          )
            add.save()
    return HttpResponse(1)

#author sctian 
def fixed_price_list(request):  
    admin_id = request.user.id
    datas = datastate_bargain.objects.filter(owner_id = admin_id)
    content = {'datas': datas}
    return render_to_response("fixed_price_list.html", content, context_instance=RequestContext(request))

#author sctian
def fixed_price_detail(request):
    admin_id = request.user.id
    admin_name = User.objects.filter(id = admin_id)[0].username
    get = request.GET
    data = datastate_bargain.objects.get(dataid_id = get["dataid"])
    post = request.POST
    if post:
        if post['feedback'] != '':
            data.detail = post['feedback']
            data.save()
        if post['judge'] == 'yes':
            data.state = 1
            data.save()
        if post['judge'] == 'no':
            data.state = -1
            data.save()
    content = {'data': data}
    return render_to_response("fixed_price_detail.html",content,context_instance=RequestContext(request))
=======
>>>>>>> hitlzp/master


@csrf_exempt
def upload_image_bargain(request):
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
    undone = alldata_bargain.objects.filter(isaval=0, owner_id = userid)
    if undone:
        if int(thetype) == 1:
            sdemo = undone[len(undone)-1].Show_demo
            add = alldata_bargain(
                          file_name = reqfile.name,
                          file_scale = thesize,
                          file = reqfile,
                          owner_id = userid,
                          isaval = 0,
                          Show_demo = sdemo
                          )
            add.save()
            alldata_bargain.objects.filter(id = undone[len(undone)-1].id).delete()
        else:
            fname = undone[len(undone)-1].file_name
            fscale = undone[len(undone)-1].file_scale
            ffile = undone[len(undone)-1].file
            add = alldata_bargain(
                          file_name = fname,
                          file_scale = fscale,
                          file = ffile,
                          Show_demo = reqfile,
                          owner_id = userid,
                          isaval = 0
                          )
            add.save()
            alldata_bargain.objects.filter(id = undone[len(undone)-1].id).delete()
            
    else:
        if int(thetype) == 1:
            add = alldata_bargain(
                          file_name = reqfile.name,
                          file_scale = thesize,
                          file = reqfile,
                          owner_id = userid,
                          isaval = 0
                          )
            add.save()
        else:
            add = alldata_bargain(
                          Show_demo = reqfile,
                          owner_id = userid,
                          isaval = 0
                          )
            add.save()
    return HttpResponse(1)
