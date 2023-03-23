# templatetags/menu_tags.py
from django import template
from django.template.loader import render_to_string
from ..models import Menu

register = template.Library()

@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    try:
        menu = Menu.objects.select_related('menu_items').get(name=menu_name)
    except Menu.DoesNotExist:
        return ''

    request = context['request']
    return render_to_string('menu/menu.html', {'menu': menu, 'request': request})
