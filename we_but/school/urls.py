from django.urls import path
from . import views

urlpatterns = [
   path('task/create/',views.task_create_or_update,name='task_create'),
   path('task/update/<int:id>/',views.task_create_or_update,name='task_update'),
   path('task/delete/<int:id>',views.task_delete,name='task_delete'),
   path('task/',views.task_list,name='task_list'),
   path('', views.welcome, name='home'),
   path('about/',views.about,name='about')
] 
