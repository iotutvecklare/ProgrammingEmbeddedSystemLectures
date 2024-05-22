import math
class Circle:
    def __init__(self, radius):
        self.r = radius

    def print_radius(self):
        print(self.r)
    def get_area(self):
        return self.r**2*math.pi

    def print_area(self):
        print(self.get_area())


    @staticmethod
    def get_perimeter():
        pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Circle = Circle(3)
    Circle.print_radius()
    Circle.print_area()
    r = Circle.get_area()
    print(r)
    print(dir())

