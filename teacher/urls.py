from django.conf.urls import url, include
from django.urls import path
from .views import teacher_list,teacher_info,upload_teacher_list


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('',teacher_list,name='teacher_list'),
    path('upload_teacher_list',upload_teacher_list,name='upload_teacher_list'),
    path('<int:teacher_id>',teacher_info,name='teacher_info'),


]