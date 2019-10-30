from django.db import models
from donor_app.models import Donor

class DonorContact(models.Model):
    CONTACT_TYPE_PHONE = 1
    CONTACT_TYPE_EMAIL = 2
    CONTACT_TYPE_FACEBOOK = 3
    contact_type_choices = {
        CONTACT_TYPE_PHONE: 'Phone',
        CONTACT_TYPE_EMAIL: 'Email',
        CONTACT_TYPE_FACEBOOK: 'Facebook'
    }

    donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
    contact = models.CharField(max_length=255)
    contact_type = models.IntegerField(choices=tuple(contact_type_choices.items()))

    def __str__(self):
        return f"{self.donor} | {self.contact_type_choices[self.contact_type]}: {self.contact}"