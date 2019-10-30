from django.shortcuts import render
from allauth.account.views import SignupView
from allauth.account.forms import SignupForm
from donor_app.forms import DonorRegisterForm

class DonorSignupView(SignupView):

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['donor_form'] = DonorRegisterForm(self.request.POST)
        return context

    def form_valid(self, form):
        response = super().form_valid(form)


        donor_form = DonorRegisterForm(self.request.POST)
        if donor_form.is_valid():
            donor = donor_form.save(commit=False)
            donor.user = self.user
            donor.save()

        return response