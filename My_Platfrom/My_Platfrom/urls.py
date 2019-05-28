"""My_Platfrom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from personal.views import login_views
from personal.views import project_views
from personal.views import module_views

urlpatterns = [
    path('index/', login_views.index),
    path('', login_views.index),  # 当url后面不输入路径的时候，也可以进入登陆页面
    path('admin/', admin.site.urls),
    path('accounts/login/', login_views.index),
    path('help/', login_views.help_manage),
    path('logout/', login_views.logout),
    path('setting/', login_views.setting_manage),

    # project管理
    path('project/', project_views.project_manage),
    path('project/add_project/', project_views.add_project),
    path('project/edit_project/<int:pid>', project_views.edit_project),

    path('module/', module_views.module_manage)


]















