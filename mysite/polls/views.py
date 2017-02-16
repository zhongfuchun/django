#coding:utf-8
from django.shortcuts import render,render_to_response
from django.http import HttpResponse
#def index(request):
#    return HttpResponse(u"欢迎光临 运维平台!  scheme:ops.zintow.com:1080/nagios")

def index(request):
    return render_to_response('index.html')

# Create your views here.
