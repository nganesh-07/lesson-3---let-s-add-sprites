import pygame
import random

pygame.init()

# custom event building for color change events
spritecolorchangeEVENT = pygame.USEREVENT + 1
backgroundcolorchangeEVENT = pygame.USEREVENT + 2

# DEFINE COLORS
# background colors
blue = pygame.Color("blue")
darkblue = pygame.Color("darkblue")
lightblue = pygame.Color("lightblue")
# sprite colors
white = pygame.Color("white")
brown = pygame.Color("brown")
lightgreen = pygame.Color("lightgreen")
lightpink = pygame.Color("lightpink")

# create a sprite class for object's movement
class Sprite(pygame.sprite.Sprite):

    def __init__(self, color, height, width): # constructor method
        super().__init__() # call to parent class constructor
        # creating sprite surface w dimensions and color
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        # sprite's rectangle width and height
        self.rect = self.image.get_rect()
        # velocity initially random direction
        self.velocity = [random.choice([-1, 1]), random.choice([-1, 1])]

    # updating sprite position
    def update(self):
        self.rect.move_ip(self.velocity)
        boundary_hit = False # false if sprite hits boundary
        if self.rect.left <= 0 or self.rect.right >= 500: # reverse position if it hits left or right boundaries
            self.velocity[0] = -self.velocity[0]
            boundary_hit = True
        if self.rect.top <= 0 or self.rect.bottom >= 400: # reverse position if it hits up or down boundaries
            self.velocity[1] = -self.velocity[1]
            boundary_hit = True

        if boundary_hit: # if boundary is hit, change color indiication
            pygame.event.post(pygame.event.Event(spritecolorchangeEVENT))
            pygame.event.post(pygame.event.Event(backgroundcolorchangeEVENT))

    # changing sprite color
    def change_color(self):
        self.image.fill(random.choice([white, brown, lightgreen, lightpink]))

# changing background color
def change_bg_color():
    global bg_color
    bg_color = random.choice([blue, lightblue, darkblue])

# create a group to hold all the sprites lol
spritelist = pygame.sprite.Group()
sp1 = Sprite(white, 20, 30)
sp1.rect.x = random.randint(0, 480)
sp1.rect.y = random.randint(0, 370)
spritelist.add(sp1)

# create game window
screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("boundary sprite") # set caption/title
bg_color = blue # set initial bg color
screen.fill(bg_color) # apply bg color

# game loop control flag
exit = False
clock = pygame.time.Clock()

# main game loop
while not exit:
        for event in pygame.event.get(): # event handling loop
            if event.type == pygame.QUIT: # if window close button is clicked, exit game
                exit = True
            elif event.type == spritecolorchangeEVENT: # if sprite color change event is triggered, change sprite color
                sp1.change_color()
            elif event.type == backgroundcolorchangeEVENT: # if bg color change event is triggered, change bg color
                change_bg_color()
        
        spritelist.update() #update all sprites
        screen.fill(bg_color) # fill w current bg color
        spritelist.draw(screen) # draw all sprites to screen

        # refresh display
        pygame.display.flip()
        clock.tick(240)

pygame.quit()