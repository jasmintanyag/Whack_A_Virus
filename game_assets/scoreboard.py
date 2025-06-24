from game_assets.base import GameElement
import winsound

class Scoreboard(GameElement):
    def __init__(self, screen):
        super().__init__(screen)
        self.score = 0
        self.turtle.goto(0, 250)
        self.turtle.color("yellow")
        self.update()

    def update(self):
        self.turtle.clear()
        self.turtle.write(f"Score: {self.score}", align="center", font=("Momcake", 24, "normal"))
        