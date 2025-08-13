import pygame


pygame.init()
screen_width, screen_height = 500, 500
screen = pygame.display.set_mode((screen_width, screen_height))

# starting position of sprite and size
x, y = 30, 30
sprite_width, sprite_height = 60, 20

# standard for letting game know when user is done
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done == True

    # to identify which keys were pressed
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]: x = -3
    if pressed[pygame.K_RIGHT]: x += 3
    if pressed[pygame.K_UP]: y -= 3
    if pressed[pygame.K_DOWN]: y += 3

    x = min(max(0, x), screen_width - sprite_width)
    y = min(max(0, y), screen_height - sprite_height)

pygame.quit()

