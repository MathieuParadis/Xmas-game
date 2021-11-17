import pygame


class Monster(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 5
        self.velocity = 5
        self.image = pygame.image.load('assets/snowman.png')
        self.image = pygame.transform.scale(self.image, (180, 180))
        self.rect = self.image.get_rect()
        self.rect.y = 510

    def receive_damage(self, amount):
        self.health -= amount

        # check if its health is <= 0
        if not self.health > 0:
            # delete monster
            self.game.all_monsters.remove(self)

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
