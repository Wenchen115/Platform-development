from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from project_app.models import Project
from django.http import HttpResponseRedirect,JsonResponse
from project_app.forms import ProjectForm


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


def delete_project(request, pid):
    """删除项目"""
    if request.method == "GET":
        try:
            project = Project.objects.get(id=pid)
        except Project.DoesNotExits:
            return HttpResponseRedirect("/project")
        else:
            project.delete()
        return HttpResponseRedirect("/project")
    else:
        return HttpResponseRedirect("/project")

@login_required
def edit_project(request, pid):
    """
    编辑项目
    :param request:
    :return:
    """
    if request.method == "GET":
        if pid:
            p = Project.objects.get(id=pid)
            form = ProjectForm(isinstance(p))
            return render(request, "project.html", {"type": "edit",
                                                    "form": form,
                                                    "id": pid})
        elif request.method == "POST":
            form = ProjectForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['name']
                describe = form.cleaned_data['describe']
                status = form.cleaned_data['status']
                p = Project.objects.get(id=pid)
                p.name = name
                p.describe = describe
                p.status = status
                p.save()
            return HttpResponseRedirect("/project")



def get_project_list(request):
    """
    接口：获取项目列表
    :param request:
    :return:
    """
    if request.method == "GET":
        project = Project.objects.all()
        project_list = []
        for pro in project:
            project_list.append(pro.name)
        return JsonResponse({"success": "True", "result": project_list})
        pass
    else:
        return JsonResponse({"success": "False", "result": "请求方法错误"})