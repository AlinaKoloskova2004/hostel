from django.urls import path
from hostel_app.views import HostelAppView, HostelAppView2, restaurant_view, room_id_view



app_name = 'hostel_app'

urlpatterns=[
    path('', HostelAppView.as_view(), name='hostel_app'),
    path('room/', HostelAppView2.as_view(), name='rooms'),
    path('restaurant/', restaurant_view, name='restaurant'),
    path('<int:pk>/', room_id_view, name='details'),
  
]
