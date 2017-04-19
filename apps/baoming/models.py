#! coding:utf-8
from __future__ import unicode_literals
from datetime import datetime

from django.db import models

from users.models import UserProfile


# Create your models here.
class Club(models.Model):
    """
    俱乐部名称
    """
    name = models.CharField(max_length=20,verbose_name=u'俱乐部名称')
    leader = models.ForeignKey(UserProfile, verbose_name=u'俱乐部管理员',default='')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u"俱乐部名称"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Player(models.Model):
    """
    参赛者
    """
    SIZE = (
        ('ml','ML'),
        ('l','L'),
        ('xl','XL'),
        ('xxl','XLL')
    )

    SHOE_SIZE_CHOICES=(
    ('38','38'),
    ('39','39'),
    ('40','40'),
    ('41','41'),
    ('42','42'),
    ('43','43')
    )
    name = models.CharField(max_length=10,verbose_name=u'姓名')
    # birday = models.DateField(verbose_name=u'生日', null=True, blank=True)
    gender = models.CharField(choices=(('male', u'男'), ('female', u'女')), default='male', verbose_name=u'性别',max_length=6)
    mobile = models.CharField(max_length=11,default='',verbose_name=u'手机号码')
    identity_card = models.CharField(max_length=18,verbose_name=u'身份证',unique=True)
    weight= models.IntegerField(verbose_name=u'体重(单位:公斤)')
    height = models.IntegerField(verbose_name=u'身高(单位:厘米)')
    swim_clothes_size = models.CharField(choices=SIZE,verbose_name=u'泳衣尺码',default='xl',max_length=5)
    t_short_size = models.CharField(choices=SIZE,verbose_name=u'T恤尺码',default='xl',max_length=5)
    shoe_size = models.CharField(choices=SHOE_SIZE_CHOICES,verbose_name=u'拖鞋尺码',default='xl',max_length=2)
    image = models.ImageField(upload_to="image/%Y/%m", default=u"image/default.png", verbose_name=u'用户图像',max_length=100)
    club = models.ForeignKey(Club,verbose_name=u'俱乐部名称')

    class Meta:
        verbose_name = u"参赛队员"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name
