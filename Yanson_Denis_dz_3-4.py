def thesaurus_adv(*args):
    some_dict = {}
    for i in sorted(args):
        some_dict.setdefault(i.split()[-1][0], {}).setdefault(i.split()[0][0], []).append(i)
    other_dict ={}
    for i in sorted(some_dict):
        other_dict[i]=some_dict[i]
    return other_dict


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
