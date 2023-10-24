class Engine2D:
    def __init__(self):
        self.canvas = []
        self.current_color = 'black'

    def add_shape(self, shape):
        self.canvas.append(shape)

    def change_color(self, color):
        self.current_color = color

    def draw(self):
        for shape in self.canvas:
            shape.draw(self.current_color)
        self.canvas = []

    def clear(self):
        self.canvas = []

class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self, color):
        print(f"Drawing Circle: ({self.x}, {self.y}) with radius {self.radius} in {color}")

class Triangle:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3

    def draw(self, color):
        print(f"Drawing Triangle: ({self.x1}, {self.y1}), ({self.x2}, {self.y2}), ({self.x3}, {self.y3}) in {color}")

class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, color):
        print(f"Drawing Rectangle: ({self.x}, {self.y}), Width: {self.width}, Height: {self.height} in {color}")

def main():
    engine = Engine2D()
    while True:
        command = input("Enter a command (add/clear/color/draw/exit): ")
        if command == 'add':
            shape_type = input("Enter the shape type (circle/triangle/rectangle): ")
            if shape_type == 'circle':
                x = float(input("Enter x coordinate: "))
                y = float(input("Enter y coordinate: "))
                radius = float(input("Enter radius: "))
                engine.add_shape(Circle(x, y, radius))
            elif shape_type == 'triangle':
                x1 = float(input("Enter x1 coordinate: "))
                y1 = float(input("Enter y1 coordinate: "))
                x2 = float(input("Enter x2 coordinate: "))
                y2 = float(input("Enter y2 coordinate: "))
                x3 = float(input("Enter x3 coordinate: "))
                y3 = float(input("Enter y3 coordinate: "))
                engine.add_shape(Triangle(x1, y1, x2, y2, x3, y3))
            elif shape_type == 'rectangle':
                x = float(input("Enter x coordinate: "))
                y = float(input("Enter y coordinate: "))
                width = float(input("Enter width: "))
                height = float(input("Enter height: "))
                engine.add_shape(Rectangle(x, y, width, height))
            else:
                print("Invalid shape type.")
        elif command == 'color':
            color = input("Enter a color: ")
            engine.change_color(color)
        elif command == 'draw':
            engine.draw()
        elif command == 'clear':
            engine.clear()
        elif command == 'exit':
            break
        else:
            print("Invalid command. Please enter 'add', 'color', 'draw', 'clear', or 'exit'.")

if __name__ == '__main__':
    main()
