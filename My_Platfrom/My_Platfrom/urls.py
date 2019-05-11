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
from personal import views

urlpatterns = [
    path('index/', views.index),
    path('', views.index),  # 当url后面不输入路径的时候，也可以进入登陆页面
    path('admin/', admin.site.urls),
    path('accounts/login/', views.index),
    path('project/', views.project_manage),
    path('module/', views.module_manage),
    path('help/', views.help_manage),
    path('logout/', views.logout)
]















