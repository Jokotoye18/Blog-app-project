from django import template
import readtime
register = template.Library()


@register.filter(name='read')
def read(html):
    return readtime.of_html(html)

