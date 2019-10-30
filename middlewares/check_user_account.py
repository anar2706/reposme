from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from datetime import datetime, time, timedelta
from donor_app.models import Donor

class CheckUserAccount:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        self.is_recently_donated(request)

        try:
            if self.is_account_closed(request):
                logout(request)
                messages.add_message(request, messages.ERROR, _("Your account is closed"))
                return redirect('account_login')
        except:
            pass

        response = self.get_response(request)

        return response

    def is_account_closed(self, request):
        return request.user.donor.is_closed

    def is_recently_donated(self, request):
        user = request.user

        if not user.is_authenticated:
            return None

        try:
            donor = Donor.objects.get(user=user)
        except:
            return None

        request.user.donor = donor

        if not donor.i_donated_recently:
            donor.expire_time_left = None
            donor.donated_recently = False
            return None

        total_seconds = (datetime.now().date() - donor.i_donated_recently).total_seconds()
        if total_seconds <= settings.DONATION_EXPIRE_TIME:
            expire_time_left = settings.DONATION_EXPIRE_TIME - total_seconds
            expire_time_left = timedelta(seconds=expire_time_left)
            donor.donated_recently = True
            donor.expire_time_left = _("Donated already. Will be available in %s days") % (expire_time_left.days)
        else:
            donor.donated_recently = False
            donor.expire_time_left = None
