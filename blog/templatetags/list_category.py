from django import template
from blog.models import CategoryModel

register = template.Library()


@register.simple_tag
def list_category():
    categories = CategoryModel.objects.all()
    return categories
