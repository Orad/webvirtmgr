from django.template import Library
import re
from django.utils.html import strip_tags

register = Library()
 

@register.filter(name='placeholder')
def placeholder(value, token):
    value.field.widget.attrs["placeholder"] = token
    return value

@register.filter(name='addclass')
def addclass(value, arg):
   return value.as_widget(attrs={'class': arg})  