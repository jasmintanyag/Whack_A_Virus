from game_assets.base import GameElement

class StartButton(GameElement):
    def __init__(self, screen, image_path):
        super().__init__(screen)
        screen.addshape(image_path)
        self.turtle.shape(image_path)
        self.turtle.goto(0, 50)
        self.turtle.showturtle()

    