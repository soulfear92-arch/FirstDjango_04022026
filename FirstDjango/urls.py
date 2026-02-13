from django.urls import path
from MainApp.views import about_view, item_view, items_view, item_detail_view, home

urlpatterns = [
    path('', home, name='home'),
    path('about/', about_view, name='about'),
    path('item/<int:id>/', item_view, name='item'),
    path('items/', items_view, name='items'),
    path('items/<int:item_id>/', item_detail_view),
]