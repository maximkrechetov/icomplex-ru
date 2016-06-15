from django.template import Library
register = Library()


@register.filter
def in_list(value, arg):
    if value is None or arg is None or len(arg) < 1:
        return False
    return value in arg
