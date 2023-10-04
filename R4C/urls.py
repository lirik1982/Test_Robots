from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/robots/', include('robots.urls')),
    path('api/v1/orders/', include('orders.urls')),
    path('api/v1/customers/', include('customers.urls')),

]
