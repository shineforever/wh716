# -*- coding: utf-8 -*-
__author__ = 'shine_forever'
__date__ = '2017/4/16 08:44'

import xadmin
from xadmin import views

from .models import Player,Club,ClubPlayer


class PlayerAdmin(object):
    list_display = ['name','gender', 'mobile','identity_card','weight','height','club']
    search_fields = ['name', 'mobile','identity_card','club__name']
    list_filter = ['name','gender', 'mobile','identity_card','club']


class ClubPlayerAdmin(object):
    list_display = ['name','gender', 'mobile','identity_card','weight','height','club']
    search_fields = ['name', 'mobile','identity_card','club__name']
    list_filter = ['name','gender', 'mobile','identity_card']
    readonly_fields = ['club']
    exclude = ['club']

    def queryset(self):
        """
        只让俱乐部管理员操作本俱乐部队员
        :return:
        """
        qs = super(ClubPlayerAdmin,self).queryset()
        if not self.user.is_superuser:  #只针对俱乐部管理员进行过滤，超级管理员不过滤；
            club = Club.objects.filter(leader__username=self.user.username)
            qs = qs.filter(club=club)
            return qs
        else:
            return qs

    def save_models(self):
        """
        保存时候，自动选择自己俱乐部名称
        :return: 
        """
        club = Club.objects.get(leader__username=self.user.username)
        self.new_obj.club = club
        self.new_obj.save()


class ClubAdmin(object):
    list_display = ['name','leader']
    search_fields = ['name']
    list_filter = ['name']



xadmin.site.register(Player,PlayerAdmin)
xadmin.site.register(ClubPlayer,ClubPlayerAdmin)
xadmin.site.register(Club,ClubAdmin)

