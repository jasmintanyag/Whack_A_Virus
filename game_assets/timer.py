from game_assets.base import GameElement

class Timer(GameElement):
    def __init__(self, screen, game_duration, callback):
        super().__init__(screen)
        self.time = game_duration
        self.callback = callback
        self.turtle.goto(0, 220)
        self.turtle.color("white")

    def start(self):
        self.time = 45
        self.update()

    def update(self):
        self.turtle.clear()
        self.turtle.write(f"Time: {self.time}s", align="center", font=("Momcake", 20, "normal"))
        if self.time > 0:
            self.time -= 1
            self.screen.ontimer(self.update, 1000)
        else:
            self.callback()