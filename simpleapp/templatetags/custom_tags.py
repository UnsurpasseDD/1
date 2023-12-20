from datetime import datetime

from django import template

register = template.Library()

@register.simple_tag()
def current_time(format_string='%b %d %Y : %H:%M:%S'):
    return datetime.utcnow().strftime(format_string)