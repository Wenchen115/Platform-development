from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from personal.models.project import Project
from django.http import HttpResponse, HttpResponseRedirect


# 登陆成功，默认跳转项目管理页面
@login_required
def project_manage(request):
    """
    项目管理
    :param request:
    :return:
    """
    project_all = Project.objects.all()
    return render(request, "project.html", {"projects": project_all, "type": "list"})


@login_required
def add_project(request):
    """
    添加项目
    :param request:
    :return:
    """
    if request.method == "GET":
        return render(request, "project.html", {"type": "add"})
    elif request.method == "POST":
        name = request.POST.get("name", "")
        describe = request.POST.get("describe", "")
        status = request.POST.get("status", "")
        if name == "":
            return render(request, "project.html", {"type": "add", "name_error": "项目名称不能为空"})
        Project.objects.create(name=name, describe=describe, status=status)
        return HttpResponseRedirect("/project")


@login_required
def edit_project(request):
    """
    编辑项目
    :param request:
    :return:
    """
    if request.method == "GET":
        return render(request, "project.html", {"type": "edit"})
