from django.urls import include, path
from module_app import views


urlpatterns = [
    # module管理
    path('', views.module_manage),
    path('add_module/', views.add_module),
    path('delete_module/<int:mid>/', views.delete_module),
    path('edit_module/<int:mid>/', views.edit_module),


]

