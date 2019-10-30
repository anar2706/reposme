# -*- coding: utf-8 -*-
"""views.py: messages extends"""

from __future__ import unicode_literals
from django.shortcuts import render
from messages_extends.models import Message
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
from django.views.decorators.csrf import csrf_exempt
from donor_app.tasks import send_donor_contacts
from donor_app.models import Donor
import json


def callable_or_bool(fn):
    if callable(fn):
        return fn()
    return fn

def get_message_by_id(message_id, user):
    message = get_object_or_404(Message, user=user, pk=message_id)
    return message
    

@csrf_exempt
def message_mark_read(request, message_id):
    if not callable_or_bool(request.user.is_authenticated):
        raise PermissionDenied

    message = get_message_by_id(message_id, request.user)
    message.read = True
    message.save()
    
    if not request.is_ajax():
        return HttpResponseRedirect(request.META.get('HTTP_REFERER') or '/')
    else:
        return HttpResponse('')

def message_mark_all_read(request):
    if not callable_or_bool(request.user.is_authenticated):
        raise PermissionDenied
    Message.objects.filter(user=request.user).update(read=True)
    if not request.is_ajax():
        return HttpResponseRedirect(request.META.get('HTTP_REFERER') or '/')
    else:
        return HttpResponse('')


def messages_list(request):
    if request.method == 'POST':
        message_id = request.POST.get('mid')
        message = get_message_by_id(message_id, request.user)
        try:
            js = json.loads(message.message)
            donor = Donor.objects.filter(user=request.user)
            send_donor_contacts.delay(to=js['email'], donor=dict(donor.values()[0]))
        except Exception as err:
            pass
        else:
            return message_mark_read(request, message_id)
        
    return render(request, 'messages_list.html')
