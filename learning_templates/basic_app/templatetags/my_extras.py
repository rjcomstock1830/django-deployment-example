from django import template

# all of this can be done with decorators...
# register = template.Library()
#
# def cut(value,arg):
#     """
#     This cuts out all values of "arg" from the string!
#     """
#
#     return value.replace(arg,'')
#
#     register.filter('cut',cut)

register = template.Library()

@register.filter(name='cut')
def cut(value,arg):
    """
    This cuts out all values of "arg" from the string!
    """

    return value.replace(arg,'')
