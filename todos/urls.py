from django.urls import path
from . import views


urlpatterns=[
      path('main/',views.todo_view, name='todo'),
]