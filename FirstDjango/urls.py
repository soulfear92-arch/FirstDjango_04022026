from django.urls import path
from MainApp.views import about_view

urlpatterns = [
    path('', about_view, name='home'),
    path('about/', about_view, name='about'),
]