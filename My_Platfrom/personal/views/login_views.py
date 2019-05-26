from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from personal.models.project import Project


# Create your views here.

def say_hello(request):
    input_name = request.GET.get("name", "")
    if input_name == "":
        return HttpResponse("请求输入？name=name")
    return render(request, "index.html", {"name": input_name})


def index(request):
    """
    登陆页面
    :param request:
    :return:
    """
    if request.method == "GET":
        return render(request, "index.html")
    else:
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        if username == "" or password == "":
            return render(request, "index.html", {"error": "用户名或密码为空"})
        user = auth.authenticate(username=username, password=password)
        print('user------>>>',user)
        if user is None:  # 如果用户名或者密码错误，那么后台返回都是none
            return render(request, "index.html", {"error": "用户名或者密码错误"})
        else:
            auth.login(request, user)  # 记录用户的登陆状态
            return HttpResponseRedirect("/project/")



@login_required
def help_manage(request):  # 帮助管理页面
    return render(request, "help.html")


@login_required
def setting_manage(request):  # 设置页面
    return render(request, "setting.html")


@login_required
def logout(request):  # 退出并清除缓存
    auth.logout(request)
    return HttpResponseRedirect("/index/")

































