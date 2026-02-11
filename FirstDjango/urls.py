from django.urls import path
from MainApp import views

urlpatterns = [
    path('', views.home),
]
from MainApp import views

urlpatterns = [
    path('about/', views, name='about'),
]