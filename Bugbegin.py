import pygame

pygame.init()

display_width = 800
display_length = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

gameDisplay = pygame.display.set_mode((display_width,display_length))
pygame.display.set_caption('ass')
clock = pygame.time.Clock()
crashed = False

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        print(event)
    pygame.display.update() #pygame.display.flip()

    clock.tick(60)

pygame.quit()
quit()
