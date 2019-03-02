from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required


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
        if user is None:
            return render(request, "index.html", {"error": "用户名或者密码错误"})
        else:
            auth.login(request, user)  # 记录用户的登陆状态
            return HttpResponseRedirect("/manage/")


# 登陆成功，跳转的页面
@login_required
def manage(request):  # 登陆成功跳转页
    return render(request, "manage.html")


@login_required
def logout(request):  # 退出并清除缓存
    auth.logout(request)
    return HttpResponseRedirect("/index/")






























