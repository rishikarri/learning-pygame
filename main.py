import pygame 
# base level module part of call -need sys to halt the program
import sys 
# import our settings from the settings module
from settings import Settings;
from hero import Hero

from pygame.sprite import Group, groupcollide

from game_functions import check_events

# initialize all of the pygame modules
pygame.init();

# screen_size = (1000, 800);


# closest color to grass
# bg_color = (82, 111, 53) 

# create a new object of type settings called game settings 
game_settings = Settings();

screen = pygame.display.set_mode(game_settings.screen_size);

pygame.display.set_caption("Monster Attack");

from enemy import Enemy

enemies = Group()
enemies.add(Enemy(screen, game_settings))



# this loop will run forever

hero = Hero(screen, game_settings)

while 1:
	check_events(hero)

	screen.fill(game_settings.bg_color)
	# draw the hero
	hero.update_me()
	hero.draw_me()
	# flip the screen = wipe it out

	for enemy in enemies.sprites():		
		enemy.update_me(hero)
		enemy.draw_me()

	pygame.display.flip();
	# need to keep redrawing the background everrrrytime! 