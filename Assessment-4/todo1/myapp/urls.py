from django.contrib import admin
from django.urls import path
from myapp.views import TodoList,TodoDetail
# Register your models here.

urlpatterns = [
    path('',TodoList.as_view()),
    path('api/Todo/<int:pk>/',TodoDetail.as_view()),
    path('admin/',admin.site.urls),
]