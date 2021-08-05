"""
5. Реализовать класс Stationery (канцелярская принадлежность).
 Определить в нем атрибут title (название) и метод draw (отрисовка).
  Метод выводит сообщение “Запуск отрисовки.”
  Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
   В каждом из классов реализовать переопределение метода draw.
   Для каждого из классов методы должен выводить уникальное сообщение.
   Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""
class Stationery:
    title = "school"

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки_ручка')

class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки_карандаш')

class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки_маркер')

pen_black = Pen()
pencil_red = Pencil()
handle_green = Handle()
pen_black.draw()
pencil_red.draw()
handle_green.draw()
