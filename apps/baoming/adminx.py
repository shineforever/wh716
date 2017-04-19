# -*- coding: utf-8 -*-
__author__ = 'shine_forever'
__date__ = '2017/4/16 08:44'

import xadmin
from xadmin import views

from .models import Player,Club


class PlayerAdmin(object):
    list_display = ['name','gender', 'mobile','identity_card','weight','height','club']
    search_fields = ['name', 'mobile','identity_card','club']
    list_filter = ['name','gender', 'mobile','identity_card','club']


class ClubAdmin(object):
    list_display = ['name','leader']
    search_fields = ['name']
    list_filter = ['name']



xadmin.site.register(Player,PlayerAdmin)
xadmin.site.register(Club,ClubAdmin)

