class Cell:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        return Cell(self.val + other.val)

    def __sub__(self, other):
        if self.val > other.val:
            return Cell(self.val - other.val)
        else:
            print('ячеек не может быть ноль или отрицательное количество')

    def __floordiv__(self, other):
        if self.val > other.val:
            return Cell(self.val // other.val)
        else:
            print('ячеек не может быть ноль или отрицательное количество')

    def __truediv__(self, other):
        if self.val > other.val:
            return Cell(self.val // other.val)
        else:
            print('ячеек не может быть ноль или отрицательное количество')

    def __mul__(self, other):
        return Cell(self.val * other.val)

    def __str__(self):
        return str(self.val)

    def make_order(self, numb):
        d = self.val // numb
        for i in range(d):
            print('*' * numb)
        if self.val % numb != 0:
            print('*' * (self.val % numb))


first_cell = Cell(10)
second_cell = Cell(3)
print(first_cell + second_cell)
print(first_cell - second_cell)
print(first_cell // second_cell)
print(first_cell * second_cell)
first_cell.make_order(3)
