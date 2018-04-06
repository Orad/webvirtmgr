from django import template
from restrict.models import RestrictInfrastructure

register = template.Library()


@register.simple_tag
def hide(title):
    titles = RestrictInfrastructure.objects.filter(is_hidden=True).values_list("title",flat=True)
    if title in titles:
        return "hide"
    return ''
