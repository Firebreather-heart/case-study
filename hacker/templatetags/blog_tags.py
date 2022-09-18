from django import template
from ..models import NewsObject

register = template.Library()

@register.inclusion_tag('lsnip.html')
def show_latest_posts(count=10):
    latest_posts = NewsObject.ext.order_by('-added')[:count]
    return {'latest_posts': latest_posts}