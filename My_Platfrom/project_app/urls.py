from django.urls import include, path
from project_app import views


urlpatterns = [
    # project管理
    path('', views.project_manage),
    path('add_project/', views.add_project),
    path('delete_project/<int:pid>/', views.delete_project),
    path('edit_project/<int:pid>/', views.edit_project),


]















