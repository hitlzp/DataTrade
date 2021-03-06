# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class alldata(models.Model):
    post_time = models.DateTimeField(default = "2012-05-15 21:05")
    dataname = models.CharField(max_length=40, null = True)
    file = models.FileField(upload_to='file')
    file_name = models.CharField(max_length=50, null = True)
    file_scale = models.CharField(max_length=20, null = True)
    exchange = models.IntegerField(default=0)
    introduce = models.TextField(null = True)
    Show_demo = models.FileField(upload_to='file')
    price = models.IntegerField(default=0)
    limit = models.IntegerField(default=0)
    limit_count = models.CharField(max_length=10, null = True)
    type = models.IntegerField(default=0)
    picture = models.FileField(upload_to='img')
    owner = models.ForeignKey(User,null = True)
    isaval = models.IntegerField(default=0)
    
class datastate(models.Model):
    state = models.IntegerField(default=0)   #
    owner = models.ForeignKey(User,null = True)
    dataid = models.ForeignKey(alldata)
    detail = models.TextField(null = True)
    
class buydata(models.Model):
    data = models.ForeignKey(alldata,null = True)
    post_time = models.DateTimeField(default = "2012-05-15 21:05")
    price = models.IntegerField(default=0)
    buyer =  models.ForeignKey(User,null = True)
    

class alldata_bargain(models.Model):

    post_time = models.DateTimeField(default = "2012-05-15 21:05")
    dataname = models.CharField(max_length=40, null = True)
    file = models.FileField(upload_to='file')
    file_name = models.CharField(max_length=50, null = True)
    file_scale = models.CharField(max_length=20, null = True)
    exchange = models.IntegerField(default=0)
    introduce = models.TextField(null = True)
    Show_demo = models.FileField(upload_to='file')
    price = models.IntegerField(default=0)
    limit = models.IntegerField(default=0)
    limit_count = models.CharField(max_length=10, null = True)
    type = models.IntegerField(default=0)
    picture = models.FileField(upload_to='img')
    owner = models.ForeignKey(User,null = True)
    isaval = models.IntegerField(default=0)
    

class datastate_bargain(models.Model):

    state = models.IntegerField(default=0)   #
    owner = models.ForeignKey(User,null = True)
    dataid = models.ForeignKey(alldata_bargain)
    detail = models.TextField(null = True)
    
class buydata_bargain(models.Model):
    post_time = models.DateTimeField(default = "2012-05-15 21:05")
    trader_id = models.ForeignKey(User,null = True,related_name='trader')
    buyer_id = models.ForeignKey(User,null = True,related_name='buyer')
    dataid = models.ForeignKey(alldata_bargain,null = True)
    price = models.IntegerField(default=0)
    state = models.IntegerField(default=0)   #state为0表示买家给卖家留言，为1表示卖家给卖家回复留言，为2表示卖家同意交易数据，为3表示卖家不同意交易数据
    buyer_detail = models.TextField(null = True)
    seller_detail = models.TextField(null = True)
    
class exchangedata(models.Model):
    post_time = models.DateTimeField(default = "2012-05-15 21:05")
    trader_id = models.ForeignKey(User,null = True,related_name='trad')
    buyer_id = models.ForeignKey(User,null = True,related_name='buye')
    dataid = models.ForeignKey(alldata,null = True)
    price = models.IntegerField(default=0)
    state = models.IntegerField(default=0)   #state为0表示买家给卖家留言，为1表示卖家给卖家回复留言，为2表示卖家同意交易数据，为3表示卖家不同意交易数据
    buyer_detail = models.TextField(null = True)
    seller_detail = models.TextField(null = True)
    link = models.TextField(null = True)
    
class exchangedata_bargain(models.Model):
    post_time = models.DateTimeField(default = "2012-05-15 21:05")
    trader_id = models.ForeignKey(User,null = True,related_name='tr')
    buyer_id = models.ForeignKey(User,null = True,related_name='bu')
    dataid = models.ForeignKey(alldata_bargain,null = True)
    price = models.IntegerField(default=0)
    state = models.IntegerField(default=0)   #state为0表示买家给卖家留言，为1表示卖家给卖家回复留言，为2表示卖家同意交易数据，为3表示卖家不同意交易数据
    buyer_detail = models.TextField(null = True)
    seller_detail = models.TextField(null = True)
    link = models.TextField(null = True)
    
class alldata_auction(models.Model):
    post_time = models.DateTimeField(default = "2012-05-15 21:05")
    dataname = models.CharField(max_length=40, null = True)
    file = models.FileField(upload_to='file')
    file_name = models.CharField(max_length=50, null = True)
    file_scale = models.CharField(max_length=20, null = True)
    exchange = models.IntegerField(default=0)
    introduce = models.TextField(null = True)
    Show_demo = models.FileField(upload_to='file')
    price = models.IntegerField(default=0)#拍卖起价
    limit = models.IntegerField(default=0)
    limit_count = models.CharField(max_length=10, null = True)
    type = models.IntegerField(default=0)
    picture = models.FileField(upload_to='img')
    owner = models.ForeignKey(User,null = True)
    isaval = models.IntegerField(default=0)
    
    rule_type = models.IntegerField(default=0)
    length_time = models.IntegerField(default=0)
    end_people = models.IntegerField(default=0)
    rule_money = models.IntegerField(default=0)
    rule_time = models.IntegerField(default=0)
    price_current = models.IntegerField(default=0)
    
class datastate_auction(models.Model):
    state = models.IntegerField(default=0)   #
    owner = models.ForeignKey(User,null = True)
    dataid = models.ForeignKey(alldata_auction)
    detail = models.TextField(null = True)
    
class aucting(models.Model):#数据拍卖过程订单
    post_time = models.DateTimeField(default = "2012-05-15 21:05")
    buyer = models.ForeignKey(User,null = True)
    price = models.IntegerField(default=0)
    dataid = models.ForeignKey(alldata_auction)
    
class aucted(models.Model):#数据拍卖结果订单
    post_time = models.DateTimeField(default = "2012-05-15 21:05")
    buyer = models.ForeignKey(User,null = True)
    price = models.IntegerField(default=0)
    dataid = models.ForeignKey(alldata_auction)
    result = models.IntegerField(default=0)