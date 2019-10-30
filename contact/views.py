from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.utils.translation import gettext_lazy as _

def contact_view(request):

    form = ContactForm(request.POST or None)
    context = {'form':form}
    if form.is_valid():
        form.save() 
        
        subject = f'Sizə {request.POST.get("email")} dan mesaj var'
        message = f'Ad : {request.POST.get("name")} \nMəzmun :\n {request.POST.get("content")}\n Email: {request.POST.get("email")}'
        email_from = 'elshadaghazade@gmail.com'
        recipient_list = ['elshadaghazade@gmail.com']
        
        send_mail(
            subject, 
            message, 
            email_from, 
            recipient_list
        )
        
        messages.success(request, _('Istəyiniz uğurla yerinə yetirildi'))

        return redirect('contact_f')
    

    

    return render(request,'contact_f.html',context)


