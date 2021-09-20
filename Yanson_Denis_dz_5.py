from random import randint


def get_jokes(intdig):
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    jokes = []
    for i in range(intdig):
        joke = nouns[randint(0, 4)] + ' ' + adverbs[randint(0, 4)] + ' ' + adjectives[randint(0, 4)]
        jokes.append(joke)
    return jokes


print(get_jokes(int(input())))
