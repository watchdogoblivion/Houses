from django import template
from homesapp.models import Location
import logging
from functools import reduce
import operator
from django.db.models import Q

logger = logging.getLogger(__name__)

register = template.Library()

@register.filter
def cut(value, arg):
    value = str(value)
    # logger.warning("Your log message is here")
    """Removes all values of arg from the given string"""
    return value.replace(arg, '')

@register.simple_tag
def check_path(request, tags, pk):
    # logger.warning(a)
    if(str(request.path) == "/homesapp/search/" or request.path == "/homesapp/"):
        tags = "location"
    elif (str(request.path) == "/homesapp/" + str(pk) + "/" or
          str(request.path) == "/homesapp/" + str(pk) + "/searchProperties/"):
        tags = "property"
    else:
        tags = ""
    return tags

@register.simple_tag
def check_persist(place, price_range, q_floors, q_beds, q_baths):
    persist = False
    price = place.price.replace(",", "")
    price = price.replace("$", "")

    price_range = price_range.replace(",", "")
    price_range = price_range.replace("$", "")
    price_range = price_range.replace("+", "")
    temp = price_range.split("-")
    range_list =  [int(i) for i in temp if i != ""]

    if len(range_list) == 1:
        range_list.append(100000000)
    elif len(range_list) == 0:
        range_list.append(0)
        range_list.append(100000000)
   
    if (((range_list[0] <= int(price) and  int(price) <= range_list[1]) or price_range == "") and 
         (place.floor == q_floors or q_floors == "") and 
         (place.beds == q_beds or q_beds == "") and 
         (place.bath == q_baths or q_baths == "")):
        persist = True
    return persist

@register.simple_tag
def loggy(l):
    logger.warning(str(l) + "///////////////////////////////////////////////")