import turtle

class GameElement:
    def __init__(self, screen):
        self.screen = screen
        self.turtle = turtle.Turtle()
        self.turtle.penup()
        self.turtle.hideturtle()