# -*- coding: UTF-8 -*-

# import builtins
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template.context import RequestContext
# 添加Django自带的分页插件 paginator
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger

#包装csrf请求，避免django认为其实跨站攻击脚本 
from django.views.decorators.csrf import csrf_exempt

import random
from .models import Student
# Create your views here.
from django.core.context_processors import csrf

def hello(request):
    return HttpResponse("我是在pptv的第一个任务！")

#访问首页
def beginAdd(request):
     return render(request, 'add.html')
#Bootstrap 测试
def test(request):
     return render(request, 'test.html')
#保存数据
@csrf_exempt
def add(request):
   # c={} POST方式获取
   id=request.POST['id']
   name=request.POST['name']
   age=request.POST['age']
   st=Student()
   if  len(id)  > 0 :
       print("id不是null")
       st.id=id;
   st.age=age
   st.name=name
   st.save()
   return HttpResponseRedirect("/q")# 转移执行query刷新操作

#删除所选数据  
def delSelect(request):  
     arr = request.GET['arr']
     blist="("+arr+")" # 根据列表构建元组
     Student.objects.extra(where=['id IN '+str(blist)+'']).delete()
     return HttpResponse("delect success")
    

#查询所有，并分页显示
def query(request):
    limit = 5  # 每页显示的记录数
    students = Student.objects.all()
    paginator = Paginator(students, limit)  # 实例化一个分页对象
    page = request.GET.get('page')  # 获取页码
    try:
        students = paginator.page(page)  # 获取某页对应的记录
    except PageNotAnInteger:  # 如果页码不是个整数
        students = paginator.page(1)  # 取第一页的记录
    except EmptyPage:  # 如果页码太大，没有相应的记录
        students = paginator.page(paginator.num_pages)  # 取最后一页的记录
    return render_to_response('curd.html',{'data':students})
#显示一条数据
def queryById(request):
    id=request.GET['id'];
    if id == "": #若无输入，则转移到query查询所有
       return HttpResponseRedirect("/q")
    bb=Student.objects.filter(id=id) #通过id 过滤结果，是一字典类型
    return render_to_response('curd.html',{'data':bb})

#更新一条数据
def showUid(request):
    id=request.GET['id'];
    bb=Student.objects.get(id=id) #得到具体数据，与filter输出返回类型不同
    return render_to_response('update.html',{'data':bb})
#删除数据
def delByID(request):
    id=request.GET['id'];
    bb=Student.objects.get(id=id)
    bb.delete() 
    return HttpResponseRedirect("/q")


#以下为测试代码，测试传递键值对
datas=[

    {"id":"1","name":"华为"},
    {"id":"2","name":"三星"},
    {"id":"4","name":"Apple"},
    {"id":"5","name":"中国"},
    {"id":"6","name":"JAVA程序员"},
    {"id":"7","name":"solr"},
    {"id":"8","name":"hadoop编程"},
    {"id":"9","name":"python"},

]
def show(request):
       return render_to_response('data.html',{'datas':datas})

