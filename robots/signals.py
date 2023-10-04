from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import get_object_or_404
from orders.models import Order
from robots.models import Robot
from django.template.loader import get_template

from customers.models import Customer


def my_send_mail(subject, message, email, customer):
    """Заглушка отправки письма."""
    print(subject)
    print(message)
    print(email)
    print(customer)
    return True


@receiver(post_save, sender=Robot)
def check_new_robots(sender, **kwargs):
    """Отправка email клиенту при появлении искомого робота."""

    instance = kwargs['instance']
    orders = Order.objects.filter(
        robot_serial=instance.serial).filter(informed=False).all()

    template = get_template('mail.html')

    for order in orders:
        customer = get_object_or_404(Customer, id=order.customer.id)
        subject = 'R4C - новые поступления'
        context = {'model': instance.serial}
        message = template.render(context=context)
        email = 'test@mail.com'
        order.informed = True
        order.save()
        my_send_mail(subject, message, email, [customer.email])
