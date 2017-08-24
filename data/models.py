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
    type = models.CharField(max_length=10, null = True)
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