class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


c = ''
d = []
v = True
while v:
    l = input()
    c = l
    if c == 'stop':
        v = False
    try:
        if not (c.isdigit() or isfloat(c)):
            raise OwnError(f'{c} не является числом')
    except OwnError as err:
        print(err)
    else:
        d.append(c)

print(d)
