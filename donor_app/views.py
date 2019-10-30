from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, TemplateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import DonorEditForm
from django.db.models import Q
from .models import *
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from .tasks import send_notification_about_required_contacts
from django.contrib import messages
from messages_extends import constants as constants_messages
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json


class DonorDashboard(LoginRequiredMixin, TemplateView):
    template_name = 'donor_dashboard.html'
    
    def get_login_url(self):
        return reverse('account_login') + "?next=" + reverse('donor_dashboard')

    def get_context_data(self, *args, **kwargs):
        context = super(LoginRequiredMixin, self).get_context_data(*args, **kwargs)

        context['total_donors'] = Donor.objects.all().count()
        context['total_donors_with_blood_group'] = Donor.objects.filter(blood_group=self.request.user.donor.blood_group).count()
        context['blood_group'] = Donor.bgroup_choices[self.request.user.donor.blood_group]

        return context


class DonorProfileEdit(LoginRequiredMixin, TemplateView):
    model = Donor
    template_name = 'donor_profile_edit.html'

    def get_context_data(self, *args, **kwargs):
        context = super(LoginRequiredMixin, self).get_context_data(*args, **kwargs)

        context['donor_edit_form'] = DonorEditForm(instance=Donor.objects.get(user=self.request.user))

        return context

    def post(self, request, **kwargs):
        donor = DonorEditForm(request.POST, instance=Donor.objects.get(user=self.request.user))
        if donor.is_valid():
            donor.save()
        else:
            return render(request, 'donor_profile_edit.html', context={
                'donor_edit_form': donor
            })

        messages.add_message(request, messages.SUCCESS, _("Your profile was changed successfully"))

        return redirect('donor_profile_edit')

@csrf_exempt
@require_http_methods(['POST'])
def give_me_your_contact(request, pk):
    
    try:
        user = Donor.objects.get(pk=pk).user
    except Exception as err:
        return JsonResponse({
            "sent": "Fail"
        })

    full_name = request.POST.get("full_name", "")
    phone = request.POST.get("phone", "")
    reason = request.POST.get("reason", "")
    email = request.POST.get("email", "")

    if not full_name.strip() or not phone.strip() or not reason.strip() or not email.strip():
        return JsonResponse({
            "sent": "Fail"
        })
    
    messages.add_message(request, constants_messages.INFO_PERSISTENT, json.dumps({
        "full_name": full_name,
        "phone": phone,
        "reason": reason,
        "email": email
    }), user=user)

    send_notification_about_required_contacts.delay(pk)

    return JsonResponse({
        'sent': 'OK'
    })


def members(request):
    return render (request,'members/members.html')