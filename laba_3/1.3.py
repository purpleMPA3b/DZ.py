import math

# Родительский класс
class GeometricFigures:
    def area(self):
        raise NotImplementedError("Метод должен быть переопределен в подклассе.")

class Primaugolnik(GeometricFigures): 
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Krug(GeometricFigures): 
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius**2

class Romb(GeometricFigures):
    def __init__(self, diagonal1, diagonal2):
        self.diagonal1 = diagonal1
        self.diagonal2 = diagonal2
    def area(self):
        return (self.diagonal1 * self.diagonal2) / 2

# Тестирование
if __name__ == "__main__":
    primaugolnik = Primaugolnik(5, 10)
    print(f"Площадь прямоугольника: {primaugolnik.area()}")
    krug = Krug(7)
    print(f"Площадь круга: {krug.area():.2f}")
    robm = Romb(5, 8)
    print(f"Площадь ромба: {robm.area()}")
