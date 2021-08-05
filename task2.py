"""
2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
 Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
  толщиной в 1 см * числосм толщины полотна. Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
"""
class Road:
    __length = None
    __width = None
    weigth = None
    thickness = None
    def __init__(self, __lenght, __width):
        self.__length = __lenght
        self.__width = __width
    def road_data(self):
        self.weigth = 25
        self.thickness = 0.05
        road_data = self.__length * self.__width * self.weigth/10 * self.thickness
        print(f'Масса асфальта дорожного покрытия равна:  {road_data}  т.')
mass_of_road = Road(20, 5000)
mass_of_road.road_data()
