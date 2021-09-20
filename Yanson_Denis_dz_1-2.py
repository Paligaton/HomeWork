def num_translate_adv(eng_number):
    translate = {'one': 'один', 'two': "два", 'three': "три", 'four': 'четрые', "five": 'пять', 'six': 'шесть',
                 'seven': 'семь', 'eight': 'воесмь', 'nine': 'девять', 'ten': 'десять', 'null': 'ноль'}
    rus_number = translate[eng_number.lower()]
    if eng_number[0].isupper():
        return rus_number.title()
    return rus_number


translate1 = {'one': 'один', 'two': "два", 'three': "три", 'four': 'четрые', "five": 'пять', 'six': 'шесть',
              'seven': 'семь', 'eight': 'воесмь', 'nine': 'девять', 'ten': 'десять', 'null': 'ноль'}
for i in translate1:
    print(num_translate_adv(i) + ' ' + num_translate_adv(i.title()))
