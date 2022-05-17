from atexit import register
from django import template

register = template.Library()

def get_utility (price, x):
    return price - x

register.filter('get_utility', get_utility)
