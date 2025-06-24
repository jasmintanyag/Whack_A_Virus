import turtle
import pygame
import os
from game_assets.image_handler import ImageHandler
from game_assets.virus import Virus
from game_assets.scoreboard import Scoreboard
from game_assets.timer import Timer
from game_assets.start_button import StartButton

class WhackAVirusGame:
    def __init__(self):
        # Initialize pygame mixer
        pygame.mixer.init()

        # Load sounds from sounds folder
        pygame.mixer.music.load(os.path.join("sounds", "background.wav"))
        self.gameover_sound = pygame.mixer.Sound(os.path.join("sounds", "gameover.wav"))
        self.score_sound = pygame.mixer.Sound(os.path.join("sounds", "score.wav"))

        # Resize virus image and store in images folder
        ImageHandler.resize_image(
            os.path.join("images", "VirusImage.png"),
            os.path.join("images", "ResizedVirusImage.gif"),
        )

        # Setup turtle screen
        self.screen = turtle.Screen()
        self.screen.setup(600, 600)
        self.screen.bgpic(os.path.join("images", "CircuitImage.png"))

        # Game elements
        self.scoreboard = Scoreboard(self.screen)
        self.virus = Virus(self.screen, os.path.join("images", "ResizedVirusImage.gif"))
        self.start_button = StartButton(self.screen, os.path.join("images", "startbutton.gif"))
        self.timer = Timer(self.screen, 20, self.end_game)

        # Bind start button
        self.start_button.on_click(self.start_game)

    def start_game(self, x, y):
        self.scoreboard.score = 0
        self.scoreboard.update()
        self.timer.start()
        self.virus.teleport()
        self.start_button.hide()
        self.virus.show()
        self.virus.on_click(self.virus_clicked)
        pygame.mixer.music.play(-1) # Loops bg music

    