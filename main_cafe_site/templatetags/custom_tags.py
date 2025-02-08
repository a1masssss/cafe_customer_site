from django import template
register = template.Library()

@register.filter
def to_uppercase(value: str):
    if not isinstance(value,str):
        return value
    return value.upper()
    

