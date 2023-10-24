from engine2d import Engine2D, Circle, Triangle, Rectangle
import pytest

def test_add_shape():
    engine = Engine2D()
    circle = Circle(0, 0, 5)
    triangle = Triangle(1, 1, 2, 2, 3, 3)
    rectangle = Rectangle(2, 2, 4, 4)
    
    engine.add_shape(circle)
    engine.add_shape(triangle)
    engine.add_shape(rectangle)
    
    assert circle in engine.canvas
    assert triangle in engine.canvas
    assert rectangle in engine.canvas

def test_change_color():
    engine = Engine2D()
    
    engine.change_color('red')
    assert engine.current_color == 'red'
    
    engine.change_color('blue')
    assert engine.current_color == 'blue'
    
    engine.change_color('green')
    assert engine.current_color == 'green'

def test_clear():
    engine = Engine2D()
    circle = Circle(0, 0, 5)
    
    engine.add_shape(circle)
    engine.clear()
    
    assert len(engine.canvas) == 0

if __name__ == '__main__':
    pytest.main()
