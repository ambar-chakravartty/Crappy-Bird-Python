import pygame
import random
import math
import os


#Physics Variables
move = True
gravity = 5
lift = 0

class Bird(pygame.sprite.Sprite):
	"""docstring for Bird"""
	def __init__(self):
		super().__init__()

		self.x = 100
		self.y = 300

		self.sprites = []
		self.sprites.append(pygame.image.load('frame1.png'))
		self.sprites.append(pygame.image.load('frame2.png'))
		self.sprites.append(pygame.image.load('frame3.png'))


		self.current = 0
		self.image = self.sprites[self.current]
		self.rect = self.image.get_rect()
		self.rect.center = [self.x,self.y]
		self.isMove = False

	def move(self):
		self.isMove = True

	def animate(self):
		self.y += gravity
		self.rect.center = [self.x,self.y]

	def fly(self):
		self.y -= lift
		self.rect.center = [self.x,self.y]	

	def update(self,i):
		if self.isMove == True:
			self.current += i 
			if int(self.current) >= len(self.sprites):
				self.current = 0 
				self.isMove = False

		self.image = self.sprites[int(self.current)]


		

def create_pipe():
	pipe_height = random.choice(heights)
	bottom_pipe = pipe_img.get_rect(center=(400,pipe_height))
	return bottom_pipe

def new_pipe():
	height = random.choice(heights)
	top_pipe = pipe_img2.get_rect(midbottom=(400,height-450))
	print(height-450)
	return top_pipe

def show_pipe(pipes,img):
	for pipe in pipes:
		screen.blit(img,pipe)

def move_pipe(pipes):
	for pipe in pipes:
		pipe.centerx -= 1
	return pipes

def crash(a,b):  #Function to detect collision between bird and pipes
	if(a.colliderect(b)):
		return True 
	else:
		return False



pygame.init()
screen = pygame.display.set_mode((400,600))
clock = pygame.time.Clock()

gameover = pygame.image.load('gameover.png')

icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

pygame.display.set_caption("Crappy Bird")

bg = pygame.image.load('background.jpg')
bg = pygame.transform.scale(bg,(400,600))

MAKEPIPE = pygame.USEREVENT
pygame.time.set_timer(MAKEPIPE, 3000)

pipe_img = pygame.image.load('pipe-green.png')
pipe_img2 =pygame.image.load('top_pipe.png')

pipe_list = []
pipes = []
heights = [700,650,500,550,600]

bird = Bird()
bird_group = pygame.sprite.Group()
bird_group.add(bird)


score = 0
font = pygame.font.Font("freesansbold.ttf",32)

running = True 
while running:
	score += 1
	print(score)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False 

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				lift = 12

		if event.type == pygame.KEYUP:
			lift = 0

		if event.type == MAKEPIPE:
			pipe_list.append(create_pipe())
			pipes.append(new_pipe())
				


	screen.fill((0,200,200))
	screen.blit(bg,(0,0))

	bird_group.draw(screen)
	bird.move()
	bird.update(0.3)
	bird.animate()
	bird.fly()

	show_pipe(pipe_list,pipe_img)
	move_pipe(pipe_list)  

	show_pipe(pipes,pipe_img2)
	move_pipe(pipes)


	for p in pipes:
		for y in pipe_list:
			if crash(bird.rect,p) or crash(bird.rect,y):
				screen.blit(gameover,(100,300))
				running = False

				
	text =  font.render(str(score),False,(255,255,255))
	screen.blit(text,(5,5))
		

	pygame.display.update()
	clock.tick(60)