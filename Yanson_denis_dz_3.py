from functools import wraps


def type_logger(func):
    @wraps(func)
    def _type_logger(*args):
        d=func(*args)
        c=type(d)
        return [d, c]
    return _type_logger


@type_logger
def calc_cube(x):
   return x ** 3


number_1 = 5
d = calc_cube(5)
print(str(number_1) + f': {d[-1]}')
print(calc_cube)


