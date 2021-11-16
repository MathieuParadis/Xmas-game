import pygame
from player import Player

class Game:
    def __init__(self):
        # generate player
        self.player = Player()
        self.pressed = {}
