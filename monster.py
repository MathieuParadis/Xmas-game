import pygame
import random


class Monster(pygame.sprite.Sprite):
    def __init__(self, game, name):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 5
        self.velocity = random.randint(1, 4)

        if name == 'monster1':
            self.image = pygame.image.load('assets/snowman.png')
        elif name == 'monster2':
            self.image = pygame.image.load('assets/reindeer.png')
        elif name == 'monster3':
            self.image = pygame.image.load('assets/elf.png')

        self.image = pygame.transform.scale(self.image, (180, 180))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 30)
        self.rect.y = 510

    def receive_damage(self, amount):
        self.health -= amount

        # check if its health is <= 0
        if self.health <= 0:
            if self.game.snow_event.is_fully_loaded():
                # delete monster if event bar is full
                self.game.all_monsters.remove(self)
                self.game.snow_event.attempt_fall()

            # reappear as a new monster (only if the event bar is not full)
            else:
                self.rect.x = random.randint(0, 30)
                self.velocity = random.randint(1, 3)
                self.health = self.max_health

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

    def move_forward(self):
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x += self.velocity

        else:
            self.game.player.receive_damage(self.attack)
