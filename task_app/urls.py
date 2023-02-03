from django.urls import path
from . import views

app_name = 'task_app'

urlpatterns = [
    path('hello/',views.hello,name='hello'),
    path('list_task/',views.list_task,name='list_task'),
    path('add_task/',views.add_task,name='add_task'),
    path('task_detail/<int:pk>',views.update_task,name='detail_task'),
    path('delete_task/<int:pk>',views.delete_task,name='delete_task'),
    path('search/',views.searchbar,name='searchbar'),
]