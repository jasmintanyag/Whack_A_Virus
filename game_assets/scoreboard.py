from game_assets.base import GameElement
import winsound

class Scoreboard(GameElement):
    def __init__(self, screen):
        super().__init__(screen)
        self.score = 0