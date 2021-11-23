import pygame
import random


class SnowBall(pygame.sprite.Sprite):
    def __init__(self, snow_event):
        super().__init__()
        self.velocity = random.randint(1, 30)
        self.damage = 10
        self.image = pygame.image.load('assets/fireball.png')
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 1080)
        self.snow_event = snow_event

    def remove(self):
        self.snow_event.all_snowballs.remove(self)

        # check if the number of comets is equal to 0
        if len(self.snow_event.all_snowballs) == 0:
            self.snow_event.reset_percent()
            self.snow_event.game.spawn_monster()
            self.snow_event.game.spawn_monster()

    def fall(self):
        self.rect.y += self.velocity

        # check if the ball falls on the ground
        if self.rect.y > 600:
            print("sol")
            self.remove()

            if len(self.snow_event.all_snowballs) == 0:
                # event is over
                # reset the bar event
                self.snow_event.reset_percent()

        # check if the ball falls on the player
        if self.snow_event.game.check_collision(self, self.snow_event.game.all_players):
            print("player touched")
            self.remove()
            self.snow_event.game.player.receive_damage(self.damage)
