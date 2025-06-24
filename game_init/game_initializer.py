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
        