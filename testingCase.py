import unittest
from SnakeGame import *

class TestSnake(unittest.TestCase):

    def test_change_direction(self):
        change(10, 0)
        self.assertEqual(aim.x, 10)
        self.assertEqual(aim.y, 0)
        
        change(0, 10)
        self.assertEqual(aim.x, 0)
        self.assertEqual(aim.y, 10)

    def test_inside(self):
        head = vector(-100, -100)
        self.assertFalse(inside(head))
        
        head = vector(0, 0)
        self.assertTrue(inside(head))

    def test_move(self):
        # Test moving snake
        start_length = len(snake)
        move()
        self.assertEqual(len(snake), start_length)
        
        
        # Test hitting wall
        snake.append(vector(-1000, 0)) 
        move()
        self.assertEqual(len(snake), start_length)

        # Test eating food
        food.x = snake[-1].x  
        food.y = snake[-1].y
        move()
        self.assertEqual(len(snake), start_length + 1)

if __name__ == '__main__':
    unittest.main()

    


