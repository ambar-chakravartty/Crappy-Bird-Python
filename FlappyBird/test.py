import pygame


pygame.init()

screen = pygame.display.set_mode((800,600))

img1 = pygame.image.load('top_pipe.png')


running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False 


	screen.blit(img1,(200,200))

	pygame.display.flip()