from django import template

register = template.Library() # регистрация фильтров,иначе Django никогда не узнает, где именно их искать и фильтры потеряются

@register.filter(name='censor')
def censor(value):
    f = open('news/templatetags/censor_list.txt', encoding="utf-8") #загружаем из файла бранные слова
    #
    str_cens = ''.join([line.replace(" ", "").lower() for line in f]).split(',')

    print(value.split())

    return ' '.join(word if not (word.lower() in str_cens) else "*" * len(word) for word in value.split())


