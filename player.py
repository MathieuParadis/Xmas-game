import pygame
from projectile import Projectile


class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('assets/player.png')
        self.image = pygame.transform.scale(self.image, (183, 192))
        self.rect = self.image.get_rect()
        self.rect.x = 430
        self.rect.y = 500

    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        # if player is not in contact with a monster
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x -= self.velocity

    def launch_projectile(self):
        self.all_projectiles.add(Projectile(self))

    def update_health_bar(self, surface):
        # define color of health bar and its background
        bar_color = (111, 210, 46)
        bg_bar_color = (60, 63, 60)

        # define the position of the health bars, their positions and their widths
        bar_position = [self.rect.x + 40, self.rect.y - 15, self.health, 5]
        bg_bar_position = [self.rect.x + 40, self.rect.y - 15, self.max_health, 5]

        # draw the health bars
        pygame.draw.rect(surface, bg_bar_color, bg_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)

    def receive_damage(self, amount):
        if self.health > 0:
            self.health -= amount

