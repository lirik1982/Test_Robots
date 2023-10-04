"""Реализация работы с клиентами."""
import json

from R4C.utils import CSRFExemptMixin
from django.views import View
from django.http import JsonResponse
from .forms import CustomerForm

from customers.models import Customer


class CustomerView(CSRFExemptMixin, View):
    def post(self, request):
        """Создание нового клиента."""

        data = json.loads(request.body.decode('utf-8'))
        form = CustomerForm(data)

        if not form.is_valid():
            return JsonResponse(form.errors)

        if Customer.objects.filter(email=data['email']):
            return JsonResponse({'error': 'already registered'})

        form.save()

        return JsonResponse(data)
