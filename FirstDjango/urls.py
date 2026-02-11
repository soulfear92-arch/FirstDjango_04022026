from django.urls import path
from MainApp.views import about_view, item_view, items_view

urlpatterns = [
    path('', about_view, name='home'),
    path('about/', about_view, name='about'),
    path('item/<int:id>/', item_view, name='item-detail'),
    path('items/', items_view),
]