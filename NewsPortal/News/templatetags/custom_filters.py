from django import template

register = template.Library()

unwanted_words = {'Редиска': 'Р******',
                  'редиска': 'h******'}


@register.filter()
def censor(value: str):
    words = value.split(' ')
    new_text = ''

    for i in range(len(words)):
        if words[i] in unwanted_words:
            words[i] = unwanted_words[words[i]]
            new_text += words[i]
            new_text += ' '
        else:
            new_text += words[i]
            new_text += ' '
    return new_text



