from game_assets.base import GameElement
import random

class Virus(GameElement):
    def __init__(self, screen, image_path):
        super().__init__(screen)
        self.screen.addshape(image_path)
        self.turtle.shape(image_path)