"""
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
 Для классов TownCar и WorkCar переопределите метод show_speed.
 При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
 Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
"""


class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def car_go(self):
        print('Car is going')

    def car_stop(self):
        print('Car is stoping')

    def car_turn(self, where):
        print(f'Car is turning {where}')

    def show_speed(self, ):
        print(f'Текущая скорость- {self.speed}')


class TownCar(Car):

    def car_for_town(self):
        print('Car for town')

    def show_speed(self):
        if self.speed > 60:
            print('Скорость превышает допустимую')
        else:
            print('Скорость в пределах нормы')


class SportCar(Car):
    def car_for_sport(self):
        print('Car for sport')


class WorkCar(Car):

    def car_for_work(self):
        print('Car for work')

    def show_speed(self):
        if self.speed > 40:
            print('Скорость превышает допустимую')
        else:
            print('Скорость в пределах нормы')


class PoliceCar(Car):
    def car_for_police(self):
        print('Car for police')


citroen = TownCar(75, 'red', 'Citroen', False)
ferrari = SportCar(210, 'yellow', 'Ferrari', False)
lada = WorkCar(45, 'white', 'Lada', False)
skoda = PoliceCar(95, 'black', 'Skoda', True)

lada.car_stop()
skoda.car_go()
ferrari.car_turn("left")
skoda.show_speed()
lada.show_speed()
