

class Car:

    is_police = False

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        print(f'{self.name} поехала')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn(self, direction):
        print(f'{self.name} повернула {direction}')

    def show_speed(self):
        print(f'{self.name} едет со скоростью {self.speed}')
        
class TownCar(Car):
    def show_speed(self):
        super(TownCar, self).show_speed()
        if self.speed > 60:
            print('скорость превышена')

class SportCar(Car):
    print('SportCar')
    
class WorkCar(Car):
    def show_speed(self):
        super(WorkCar, self).show_speed()
        if self.speed > 40:
            print('скорость превышена')

class PoliceCar(Car):
    is_police = True

d=TownCar(50, 'Зеленая', 'Lada')
d.show_speed()
d=WorkCar(70, 'Желтая', 'Audi')
print(d.is_police)
d=PoliceCar(70, 'Желтая', 'Audi')
print(d.is_police)
d.show_speed()
d.turn('налево')
d.turn('направо')
d.stop()