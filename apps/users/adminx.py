# -*- coding: utf-8 -*-
__author__ = 'shine_forever'
__date__ = '2017/4/15 23:53'


import xadmin
from xadmin import views

from .models import UserProfile

class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True

class GlobalSettings(object):
    site_title = "武汉市泳协716报名管理后台"
    site_footer = "武汉市泳协"
    # menu_style = "accordion"    #xadmin菜单收起来


class UserProfileAdmin(object):
    list_display = ['nick_name','gender', 'address','mobile']
    search_fields = ['nick_name','gender', 'address','mobile']
    list_filter = ['nick_name','gender', 'address','mobile']



# xadmin.site.register(UserProfile,UserProfileAdmin)

xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSettings)



