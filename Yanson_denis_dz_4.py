from functools import wraps


def val_checker(func_1):
    @wraps(func_1)
    def val_che(func):
        @wraps(func)
        def val_check(arg):
            if not func_1(arg):
                raise ValueError(f'wrong val {arg}')
            else:
                return func(arg)
        return val_check
    return val_che





@val_checker(lambda x: x > 0)
def calc_cube(x):
   return x ** 3


print(calc_cube)
print (calc_cube(-5))