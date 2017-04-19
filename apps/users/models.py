#! coding:utf-8
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserProfile(AbstractUser):
    """
    俱乐部管理员信息
    """
    nick_name = models.CharField(max_length=50, verbose_name=u'昵称', default=u'')
    mobile = models.CharField(max_length=11, null=True, blank=True)
    # image = models.ImageField(upload_to="image/%Y/%m", default=u"image/default.png", max_length=100)

    class Meta:
        verbose_name = u"俱乐部管理员"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username