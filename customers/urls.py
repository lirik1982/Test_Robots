from django.urls import path

from .views import CustomerView


urlpatterns = [
    path('add', CustomerView.as_view(), name='add_cutome')
]
