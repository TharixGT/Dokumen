# coding: utf-8
import copy

from django import template
from django.http import HttpRequest

register = template.Library()


@register.simple_tag
def querystring(request, key, value, *args, **kwargs):
    if not isinstance(request, HttpRequest):
        raise ValueError('First parameter must be a request object')
    query = copy.deepcopy(request.GET)
    query[key] = value
    return query.urlencode()


@register.filter
def pagination_range(page_obj, length):
    num_pages = page_obj.paginator.num_pages
    current = page_obj.number
    variation = length / 2 if num_pages > length else length
    min_value = (current - variation) if current - variation > 0 else 1
    max_value = current + variation if current + variation < num_pages else num_pages
    left_block = []
    right_block = []
    page_range = range(min_value, max_value + 1)
    if num_pages > length:
        if page_range[0] != 1:
            left_block += [1]
            if page_range[0] != 2:
                left_block += ['...']
        if page_range[-1] != num_pages:
            if page_range[-1] != num_pages - 1:
                right_block += ['...']
            right_block += [num_pages]
    return left_block + page_range + right_block


@register.filter
def querystring_without_page(request):
    query = copy.deepcopy(request.GET)
    query.pop('page', None)
    return query.urlencode()
