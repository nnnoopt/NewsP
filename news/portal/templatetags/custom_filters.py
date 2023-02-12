from django import template


register = template.Library()


Words = [
    'Дурак',
    'Идиот'
]

@register.filter()
def my_filter(value):

    for word in Words:
        value = value.replace(word, '*' * len(word))
    return value