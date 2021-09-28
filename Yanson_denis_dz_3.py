from itertools import islice


def gen(tut, klass):
    for i, v in enumerate(tut):
        if i < len(klass):
            cort = (v, klass[i])
        else:
            cort = (v, 'None')
        yield cort


tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А'
]
gens = gen(tutors,klasses)
print(list(islice(gens, len(tutors))))
print(next(gens))
