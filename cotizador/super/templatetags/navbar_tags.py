from django import template
register = template.Library()


@register.simple_tag
def active_page(request, view_name):
    """Tag utilizado para devolver una clase css si esta activo el url

    Args:
        request (request): Current Request
        view_name (String): Url name a evaluar

    Returns:
        TYPE: Description
    """
    from django.core.urlresolvers import resolve, Resolver404

    if not request:
        return ''
    try:
        if view_name == resolve(request.path_info).url_name:
            return "active"
        else:
            return ''
    except Resolver404:
        return ''


@register.simple_tag
def active_page_app(request, view_name):
    """Tag utilizado para devolver una clase css si esta activo el url

    Args:
        request (request): Current Request
        view_name (String): Url name a evaluar

    Returns:
        TYPE: Description
    """
    from django.core.urlresolvers import resolve, Resolver404

    if not request:
        return ''
    try:
        view_name = view_name.split('-')
        url_name = resolve(request.path_info).url_name.split('-')
        if view_name[0] == url_name[0]:
            return 'active'
        else:
            return ''
    except Resolver404:
        return ''
