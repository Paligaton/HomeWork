class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        super(Pen, self).draw()
        print(f'Ручка {self.title} отрисована')


class Pencil(Stationery):
    def draw(self):
        super(Pencil, self).draw()
        print(f'Карандаш {self.title} отрисован')


class Handle(Stationery):
    def draw(self):
        super(Handle, self).draw()
        print(f'Маркер {self.title} отрисован')


show = [Pen('синяя'), Pencil('розовый'), Handle('черный')]
for i in show:
    i.draw()
