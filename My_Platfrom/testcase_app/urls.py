from django.urls import include, path
from testcase_app import views


urlpatterns = [
    # project管理
    path('', views.testcase_manage),
    path('debug', views.debug),


]

