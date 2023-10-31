class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter
        self.radius = diameter/2

    def calculate_circumference(self):
        circumference = self.diameter*Circle.__pi
        return circumference

    def calculate_area(self):
        area = Circle.__pi*self.radius*self.radius
        return area

    def calculate_area_of_sector(self, angle):
        sector = (angle/360)*Circle.__pi*self.radius*self.radius
        return sector
circle = Circle(10)
angel = 5

print(f'{circle.calculate_circumference():.2f}')
print(f'{circle.calculate_area():.2f}')
print(f'{circle.calculate_area_of_sector(angel):.2f}')


