import pygame
from game import Game
pygame.init()


# generate the window of the game
pygame.display.set_caption("Comet game")
screen = pygame.display.set_mode((1080, 720))

# load background image
background = pygame.image.load('assets/bg.png')

# load banner image
banner = pygame.image.load('assets/banner.png')
banner_rect = banner.get_rect()
banner_rect.x = (screen.get_width() / 2.0) - (banner.get_width() / 2.0)
banner_rect.y = (screen.get_height() / 2.0) - (banner.get_height() / 2.0)

# load play button
play_button = pygame.image.load('assets/play.jpg')
play_button = pygame.transform.scale(play_button, (400, 200))
play_button_rect = play_button.get_rect()
play_button_rect.x = (screen.get_width() / 2.0) - (play_button.get_width() / 2.0)
play_button_rect.y = (screen.get_height() / 2.0) - (play_button.get_height() / 2.0) + 150

# launch game
game = Game()

running = True

# game running as long as running is true
while running:

    # apply bg image
    screen.blit(background, (0, 0))

    # check if the game started or not
    if game.is_playing:
        game.update(screen)
    else:
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)

    # update the screen
    pygame.display.flip()

    # if player close the window
    # check all events
    for event in pygame.event.get():
        # if event is closing window
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        # if player press a key
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # check if the mouse if in contact with play_button
            if play_button_rect.collidepoint(event.pos) and game.is_playing == False:
                game.start_game()
