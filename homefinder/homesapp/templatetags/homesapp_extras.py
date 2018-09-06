from django import template
import logging

logger = logging.getLogger(__name__)

register = template.Library()

@register.filter
def set_value(value):
    # logger.warning("Check Setting")
    return value

@register.filter
def cut(value, arg):
    value = str(value)
    # logger.warning("Your log message is here")
    """Removes all values of arg from the given string"""
    return value.replace(arg, '')

@register.simple_tag
def check_path(request, tags):
    # logger.warning(a)
    if(str(request.path) == "/homesapp/search/" or request.path == "/homesapp/"):
        tags = True
    else:
        tags = False
    return tags
