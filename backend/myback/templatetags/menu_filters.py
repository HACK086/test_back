# templatetags/menu_filters.py
from django import template

register = template.Library()

@register.filter
def tree(items, current_path):
    def build_tree(parent):
        result = []
        for item in items.filter(parent=parent).order_by('title'):
            item.active = (item.get_url() == current_path)
            item.children = build_tree(item)
            result.append(item)
        return result

    return build_tree(None)
