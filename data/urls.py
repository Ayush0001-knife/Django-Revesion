from django.urls import path
from . import views

urlpatterns = [
      path('<int:id>/', views.example_view, name='example_view'), 
]