from django import template
register = template.Library()

@register.filter(name='bek')
def Max(abs):
    if len(abs)>5:
        return 'False'
    else: 
        return 'True'