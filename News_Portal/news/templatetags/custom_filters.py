from django import template

register = template.Library()


censor_list = ['червяк', 'косипоша', 'жалкий']

# Регистрируем наш фильтр под именем currency, чтобы Django понимал,
# что это именно фильтр для шаблонов, а не простая функция.
@register.filter(name = "censor")

def currency(value):
   for word in censor_list:
      value = value.replace(word, '*' * len(word))
   return value
