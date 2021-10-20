class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


class Storage:
    def __init__(self, some_dict=[]):
        try:
            if not isinstance(some_dict, list):
                raise OwnError('вы ввели информацию не правильного формата')
        except OwnError as err:
            print(err)
            self.items=[]
            return
        else:
            self.items = some_dict
        print(self.items)

    def add(self, item, number):
        try:
            if not number.isdigit() and not isinstance(number, int):
                raise OwnError('количество предметов не правильного формата')
        except OwnError as err:
            print(err)
            return
        if len(self.items) > 0:
            for i, v in enumerate(self.items):
                if item == v[0]:
                    v[1] += int(number)
                    return
        self.items.append([item, int(number)])

    def remove(self, item, number):
        try:
            if  not number.isdigit() and not isinstance(number, int) :
                raise OwnError('количество предметов не правильного формата')
        except OwnError as err:
            print(err)
            return
        for i, v in enumerate(self.items):
            if item == v[0] and int(number) == v[1]:
                self.items.remove[i]
                return
            elif item == v[0]:
                try:
                    if v[1] < int(number):
                        raise OwnError('данных предметов на складе меньше чем вы запрашиваете')
                except OwnError as err:
                    print(err)
                    return
                else:
                    v[1] -= int(number)
                    return
        try:
            raise OwnError('данных предметов нет на складе')
        except OwnError as err:
            print(err)


class Tech:
    def __init__(self, info_in, info_out):
        self.info_in = info_in
        self.info_out = info_out


class Printer(Tech):
    def __init__(self, atr):
        self.info_in = False
        self.info_out = True
        self.atr = atr


class Xerox(Tech):
    def __init__(self, atr):
        self.info_in = True
        self.info_out = True
        self.atr = atr


class Scaner(Tech):
    def __init__(self, atr):
        self.info_in = True
        self.info_out = False
        self.atr = atr


store = Storage(1)
scn = Scaner('Green')
xrx = Xerox('Yellow')
prnt = Printer('Red')
print(store.items)
store.add(scn, '5')
print(store.items)
store.remove(scn, '4')
print(store.items)
store.add(scn, '5')
print(store.items)
store.remove(scn, '7')
store.add(xrx, '5')
print(store.items)
store.remove(xrx, '4')
store.remove(scn, '1')
print(store.items)