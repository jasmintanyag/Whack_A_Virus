from game_assets.base import GameElement
import random

class Virus(GameElement):
    def __init__(self, screen, image_path):
        super().__init__(screen)
        self.screen.addshape(image_path)
        self.turtle.shape(image_path)

    def show(self):
        self.turtle.showturtle()

    def hide(self):
        self.turtle.hideturtle()

    def teleport(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 230)
        self.turtle.goto(x, y)
        self.screen.ontimer(self.teleport, 200)

    def on_click(self, callback):
        self.turtle.onclick(callback)