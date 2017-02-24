# a file for all of our game functions to clean up main.py
import pygame
import sys


def check_events(hero):
	for event in pygame.event.get(): 
		# this means the user clicked on the red x
		if event.type == pygame.QUIT: 
			sys.exit() 
			# halt the entire program
			# Stop the game, the user wants to stop playing			
		elif event.type == pygame.KEYDOWN:
			print event.key

			if event.key == pygame.K_RIGHT:
				print "pressed right"
				hero.moving_right = True

			if event.key == pygame.K_LEFT:
				print "pressed left"
				hero.moving_left = True
			if event.key == pygame.K_UP:
				print "pressed up"
				hero.moving_up = True
			if event.key == pygame.K_DOWN:
				print "pressed down"
				hero.moving_down = True

		elif event.type == pygame.KEYUP: 

			if event.key == pygame.K_RIGHT:
				print "pressed right"
				hero.moving_right = False

			if event.key == pygame.K_LEFT:
				print "pressed left"
				hero.moving_left = False
			if event.key == pygame.K_UP:
				print "pressed up"
				hero.moving_up = False
			if event.key == pygame.K_DOWN:
				print "pressed down"
				hero.moving_down = False