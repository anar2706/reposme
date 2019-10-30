from django import template
from django.conf import settings
from datetime import datetime, time, timedelta
from django.utils.translation import gettext_lazy as _
import json

register = template.Library()

json_decode_string = ""
json_decode_dict = {}

@register.filter(name='contains')
def contains(string, val):
    return val in string

@register.filter(name='seq_counter')
def seq_counter(seq):
    return len(seq)

@register.filter(name='count_persistent_messages')
def count_persistent_messages(messages):
    # print(dir(messages))
    return len(tuple(filter(lambda x: "persistent" in x.tags, messages)))

@register.filter(name='json_decode')
def json_decode(string, keyword):
    global json_decode_string, json_decode_dict

    if json_decode_string == string:
        return json_decode_dict.get(keyword)

    try:
        js = json.loads(str(string))
        json_decode_dict = js
        json_decode_string = string
        return js.get(keyword)
    except:
        return string


@register.filter(name='donor_filter')
def donor_filter(donor):
    if not donor.i_donated_recently:
        return donor

    total_seconds = (datetime.now().date() - donor.i_donated_recently).total_seconds()
    if total_seconds <= settings.DONATION_EXPIRE_TIME:
        expire_time_left = settings.DONATION_EXPIRE_TIME - total_seconds
        expire_time_left = timedelta(seconds=expire_time_left)
        donor.donated_recenty = True
        donor.expire_time_left = _("Donated already. Will be available in %s days") % (expire_time_left.days)
    else:
        donor.donated_recenty = False
        donor.expire_time_left = 0

    return donor
