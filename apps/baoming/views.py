#! coding:utf-8

from django.shortcuts import render,HttpResponse
from django.views.generic import View
from django.db.models import Q

from baoming.models import Player
# Create your views here.

class SearchView(View):
    """
    身份证查询
    """
    def get(self,request):
        return render(request,'search.html',{})
    def post(self,request):
        identity_card = request.POST.get('identity_card','')
        if Player.objects.filter(identity_card=identity_card):
            player = Player.objects.get(identity_card=identity_card)
            return render(request,'player_detail.html',{
                    'player':player
                })
        else:
            return HttpResponse(u"找不到该信息，请与报名俱乐部管理员联系！")
