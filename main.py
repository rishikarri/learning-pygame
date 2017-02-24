import pygame 
# base level module part of call -need sys to halt the program
import sys 

# import our settings from the settings module
from settings import Settings;
from hero import Hero

from pygame.sprite import Group, groupcollide

from game_functions import check_events

from button import Start_Button
pygame.init();

game_settings = Settings();
screen = pygame.display.set_mode(game_settings.screen_size);

start_button = Start_Button(screen)


# initialize all of the pygame modules


# screen_size = (1000, 800);


# closest color to grass
# bg_color = (82, 111, 53) 

# create a new object of type settings called game settings 




pygame.display.set_caption("Monster Attack");

from enemy import Enemy

# Make a group for the hero to belong to so we can use groupcollide

hero = Hero(screen, game_settings)

hero_group = Group()
hero_group.add(hero)

enemies = Group()
enemies.add(Enemy(screen, game_settings))



# this loop will run forever



while 1:
	check_events(hero)

	screen.fill(game_settings.bg_color)
	# draw the hero
	
	if game_settings.game_active: 
		enemy.update_me(hero)
	enemy.draw_me()

	for hero in hero_group.sprites():		
		hero.update_me()
		hero.draw_me()
	# flip the screen = wipe it out

	for enemy in enemies.sprites():		
		enemy.update_me(hero)
		enemy.draw_me()

	hero_died = groupcollide(hero_group, enemies, True, False);

	if hero_died:
		print "You lost!"
		game_settings.game_active = False

	start_button.draw_button()

	pygame.display.flip();
	# need to keep redrawing the background everrrrytime! 