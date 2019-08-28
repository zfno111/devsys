from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Asset(models.Model):
    """    所有资产的共有数据表    """
    #主机名
    name =  models.CharField(max_length=64, unique=True, verbose_name="资产名称")     # 不可重复
    #环境
    envir = models.CharField(max_length=64, unique=False, verbose_name="主机所在环境")
    #操作系统类型
    ossys =  models.ForeignKey('System', null=True, blank=True, verbose_name='操作系统类型', on_delete=models.SET_NULL)
    #用户名
    userid = models.CharField(max_length=32,unique=False,verbose_name="用户名")
    #密码
    userpasswd =  models.CharField(max_length=32,unique=False,verbose_name="用户密码")
    #内网IP
    ipin = models.CharField(max_length=32,unique=True,verbose_name="内网IP")
    #外网IP
    ipout = models.CharField(max_length=32,unique=False,verbose_name="外网IP")
    #CPU信息
    cpu =  models.CharField(max_length=16,verbose_name="CPU信息")
    #内存信息
    mem = models.CharField(max_length=16,verbose_name="内存")
    #描述信息
    desc =  models.CharField(max_length=32,verbose_name="描述信息")
    #系统盘
    sysdisk = models.CharField(max_length=16,verbose_name="系统盘")
    #数据盘
    datadisk = models.CharField(max_length=16,verbose_name="数据盘")
    #带宽
    bandwidth = models.CharField(max_length=16,verbose_name="带宽")
    #安全组
    secgroup = models.CharField(max_length=16,verbose_name="安全组")
    #分组
    group =  models.CharField(max_length=32,verbose_name="分组")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '资产总表'
        verbose_name_plural = "资产总表"


class System(models.Model):
    name =  models.CharField(max_length=64,verbose_name="操作系统类型")
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '操作系统类型'
        verbose_name_plural = "操作系统类型"



