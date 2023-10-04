from django.urls import path
from .views import OrdersView

urlpatterns = [
    path('add', OrdersView.as_view(), name='add_order'),
]
