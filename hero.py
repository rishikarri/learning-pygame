import pygame

# this will get the sprite class from pygame.sprite. Our hero will be an instance of the sprite object
from pygame.sprite import Sprite


class Hero(Sprite):
	# initialize class properties
	def __init__(self, screen, settings):
		# go to your parent class and pass up the self
		super(Hero, self).__init__()
		self.image = pygame.image.load('Enemies-Allies/archer3.png')
		# self.image = pygame.transform.scale(self.image, (100, 85))
		self.screen = screen
		# create a rect prop that will lbe the dimensions of the image 
		# it's available in get_rect because this is a pygame image
		self.rect = self.image.get_rect();
		print self.image.get_rect();
		# Now that w ehave the screen object from the main, get teh size of hte screen
		self.screen_rect = screen.get_rect();
		print self.screen_rect;

		# this will put the middle of the hero at the middle of the screen
		self.rect.centery = self.screen_rect.centery
		# this will put the left side of our hero at the left side of our scrreen 
		self.rect.left = self.screen_rect.left;
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False
		self.speed = settings.hero_speed

	def update_me(self):
		# if user is pushing left, move my self.rect left and so on


		if self.moving_right:
			self.rect.centerx += 10 * self.speed
			

		elif self.moving_left:
			self.rect.centerx -= 10 * self.speed
			

		if self.moving_down:
			self.rect.centery += 10 * self.speed
			
			
		elif self.moving_up:
			self.rect.centery -= 10 * self.speed
			



	def draw_me(self):

		self.screen.blit(source = self.image, dest = self.rect);
