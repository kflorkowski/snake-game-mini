from turtle import Turtle
from random import randrange

class Food(Turtle):
    """
    Represents the food object in the Snake game.
    Inherits from the Turtle class to display a red circular item
    that appears in random positions on the screen.
    """
    def __init__(self):
        """Initialize the food with shape, color, and initial random position."""
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed(0)
        self.refresh()

    def refresh(self):
        """
        Move the food to a new random location within the play area.
        Called whenever the snake eats the food.
        """
        random_x = randrange(-280, 280, 20)
        random_y = randrange(-280, 280, 20)
        self.goto(random_x, random_y)
