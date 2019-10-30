# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.core.mail import send_mail
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy
from django.conf import settings
from django.contrib.auth.models import User

@shared_task
def send_notification_about_required_contacts(user_id):
    message = _(f"""
            Please, follow <a href="{reverse_lazy('give_me_your_contact', kwargs={'pk': user_id})}">this link</a> to see requesters.
        """)

    send_mail(
        subject=_(f"You have new requester for your phone number"),
        message=message,
        html_message=message,
        from_email='elshadaghazade@gmail.com',
        recipient_list=[User.objects.get(pk=user_id).email],
        fail_silently=False,
    )

@shared_task
def send_donor_contacts(to, donor):
    message = _(f"{donor['first_name']} {donor['last_name']}'s phone number is: <a href='tel:{donor['phone']}'>{donor['phone']}</a>")

    send_mail(
        subject=_(f"Donor {donor['first_name']} {donor['last_name']} sent you contact information"),
        html_message=message,
        message=message,
        from_email=settings.EMAIL_FROM,
        recipient_list=[to],
        fail_silently=False
    )