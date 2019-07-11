from django.contrib import admin
from django.urls import include, path
from user_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # 用户应用
    path('index/', views.index),
    path('', views.index),  # 当url后面不输入路径的时候，也可以进入登陆页面
    path('accounts/login/', views.index),
    path('help/', views.help_manage),
    path('logout/', views.logout),
    path('setting/', views.setting_manage),

    # project管理
    path('project/', include('project_app.urls')),

    # module管理
    path('module/', include('module_app.urls')),

    # 用例管理
    path('testcase/', include('testcase_app.urls'))





]















