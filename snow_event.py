import pygame
from snowball import SnowBall


class SnowFallEvent:
    def __init__(self, game):
        self.percent = 0
        self.percent_speed = 80
        self.game = game
        self.fall_mode = False

        # define a group of sprite to store the snowballs
        self.all_snowballs = pygame.sprite.Group()

    def add_percent(self):
        self.percent += self.percent_speed / 100

    def reset_percent(self):
        self.percent = 0

    def is_fully_loaded(self):
        return self.percent >= 100

    def attempt_fall(self):
        if self.is_fully_loaded() and len(self.game.all_monsters) == 0:
            self.snow_fall()
            self.fall_mode = True

    def snow_fall(self):
        # loop for a value between 1 to 10
        for i in range(1, 10):
            self.all_snowballs.add(SnowBall(self))

    def update_bar(self, surface):
        self.add_percent()

        # define color of the bar and its background
        bar_color = (187, 11, 11)  # red
        bg_bar_color = (0, 0, 0)  # black

        # define the position of the health bars, their positions and their widths
        bar_position = [0, surface.get_height() - 20, surface.get_width() / 100 * self.percent, 10]
        bg_bar_position = [0, surface.get_height() - 20, surface.get_width(), 10]

        # draw the bars
        pygame.draw.rect(surface, bg_bar_color, bg_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)
