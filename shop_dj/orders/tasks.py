from celery import shared_task
from django.core.mail import send_mail
from .models import Order


@shared_task
def order_created(order_id):
    """
    Задание для отправки уведомления по электронной почте
    при успешном создании заказа.
    """
    order = Order.objects.get(id=order_id)
    subject = f'Заказ №{order.id}'
    message = f'Уважаемый {order.first_name}, \n\n'
    'Вы успешно разместили заказ.'\
    f'Номер Вашего заказа №{order.id}.'
    mail_sent = send_mail(subject, message, 'berkepisti@gufum.com', [order.email])
    return mail_sent