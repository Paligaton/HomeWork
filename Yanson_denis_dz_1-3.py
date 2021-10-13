import time


class TrafficLight:
    __color = ['красный', 'желтый', 'зеленый']

    def running(self):
        check_while = True
        while check_while is True:
            print(self.__color[0])
            time.sleep(7)
            print(self.__color[1])
            time.sleep(2)
            print(self.__color[2])
            time.sleep(1)
            print('Введите + если хотите запустить светофор еще раз:')
            if input() != '+':
                check_while = False


class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width
    def counting(self, weight, thickness):
        return self._length*self._width*weight*thickness/1000


class Worker:
    name = 'Ivan'
    surname = 'Not_Ivan'
    position = 'Dealer'
    _income = {"wage": 50, "bonus": 10}

class Position(Worker):

    def get_full_name(self):
        return Worker.name + ' ' + Worker.surname

    def get_total_income(self):
        return Worker._income['wage'] + Worker._income['bonus']


d = TrafficLight()
d.running()
r = Road (5000, 20)
print(str(r.counting(25,5)) + ' т' )
w = Position()
print(w.get_full_name())
print(w.get_total_income())