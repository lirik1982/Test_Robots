"""Модуль реализации работы с заказами."""

import json

from customers.models import Customer
from django.shortcuts import get_object_or_404
from django.views import View
from R4C.utils import CSRFExemptMixin
from .forms import NewOrderForm
from orders.models import Order
from django.http import JsonResponse


class OrdersView(CSRFExemptMixin, View):
    def post(self, request):
        """Создание нового заказа."""

        data = json.loads(request.body.decode('utf-8'))
        data['informed'] = False

        form = NewOrderForm(data)

        if not form.is_valid():
            return JsonResponse(form.errors)

        Order.objects.create(
            customer=get_object_or_404(Customer, id=data['customer']),
            robot_serial=data['robot_serial'],
            informed=data['informed'],
        )

        return JsonResponse(data)
