import re
from decimal import Decimal

from django.template import Library
from django.utils.html import strip_tags

register = Library()


@register.filter(name='placeholder')
def placeholder(value, token):
    value.field.widget.attrs["placeholder"] = token
    return value

@register.filter(name='addclass')
def addclass(value, arg):
    return value.as_widget(attrs={'class': arg})

@register.filter(name='has_perm')
def has_perm(value, perm):
    return value.has_perm(perm)

@register.filter(name='convert_time')
def convert_time(value):
    time = value/Decimal(60.0)
    hours = int(time)
    minutes = (time*60) % 60
    seconds = (time*3600) % 60  
    return "%d:%02d:%02d" % (hours, minutes, seconds)