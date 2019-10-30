exit()

import os
import sys
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blood_bank_project.settings')


import django
django.setup()


from django.core.mail import send_mass_mail, send_mail
from django.contrib.auth.models import User
from donor_app.models import Donor

def make_message(email):
    title = 'Yenicə qan vermiş donorlar üçün yenilik'
    body = """
    <h1><a href="https://xilaset.org">Xilaset.org</a> yenilik.</h1>
    <p><a href="https://xilaset.org">Xilaset.org</a> donor kimi qeydiyyatdan keçmiş istifadəçilərin rahatçılığı üçün sistemə əlavələr etmişdir. Artıq qan vermiş donorları 6 ay müddətində zənglərlə narahat etməyəcəklər. Bunun üçün qan vermiş donor <a href="https://xilaset.org/donated-already/">Mən artıq qan vermişəm</a> bölməsinə daxil olaraq oradan öz əlaqə vasitələrini 6 ay müddətində gizlədə bilərlər.</p>

    <p><strong>Hörmətlə, Elşad Ağayev</strong></p>
    """

    return dict(subject=title, html_message=body, message=body, from_email='xilaset@gmail.com', recipient_list=email)

emails = map(make_message, set(Donor.objects.all().values_list('user__email')))

for email in emails:
    send_mail(**email)  
