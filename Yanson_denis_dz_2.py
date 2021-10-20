class OwnError(ZeroDivisionError):
    def __init__(self, txt):
        self.txt = txt

inp_data = input("Введите делимое число: ")
inp_data_2 = input("Введите делитель: ")

try:
    inp_data = int(inp_data)
    inp_data_2 = int(inp_data_2)
    if inp_data_2 == 0:
        raise OwnError("на ноль делить нельзя!")
except OwnError as err:
    print(err)
else:
    print(f"Результат: {int(inp_data)/int(inp_data_2)}")