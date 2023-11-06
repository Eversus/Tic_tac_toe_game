from pprint import pprint

from django import template

register = template.Library()


censor_list = ['редиска', 'поограмист', 'васисуалий']

# Регистрируем наш фильтр под именем currency, чтобы Django понимал,
# что это именно фильтр для шаблонов, а не простая функция.
@register.filter(name = "censor")

def currency(value):
   bad_words = ['редиска', 'поограмист', 'васисуалий']
   for word in bad_words:
      value = value.replace(word, '*' * len(word))
   return value
