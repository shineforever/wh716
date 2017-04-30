# -*- coding: utf-8 -*-
__author__ = 'shine_forever'
__date__ = '2017/4/16 08:44'

import xadmin
from xadmin import views

from .models import Player,Club


class PlayerAdmin(object):
    list_display = ['name','gender', 'mobile','identity_card','weight','height','club']
    search_fields = ['name', 'mobile','identity_card','club__name']
    list_filter = ['name','gender', 'mobile','identity_card','club']

    def queryset(self):
        """
        只让俱乐部管理员操作本俱乐部队员
        :return:
        """
        qs = super(PlayerAdmin,self).queryset()
        if self.user.is_superuser == False:  #只针对俱乐部管理员进行过滤，超级管理员不过滤；
            club = Club.objects.filter(leader__username=self.user.username)
            qs = qs.filter(club=club)
            return qs
        else:
            return qs



class ClubAdmin(object):
    list_display = ['name','leader']
    search_fields = ['name']
    list_filter = ['name']



xadmin.site.register(Player,PlayerAdmin)
xadmin.site.register(Club,ClubAdmin)

