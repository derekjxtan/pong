import sys
import pygame
from setting import Settings
from right_paddle import Rpaddle
from left_paddle import Lpaddle
from ball import Ball
from button import Button
from stats import Stats
from scoreboard import Scoreboard
from winner_msg import Winnermsg
import game_functions as gf

def run_game():
	#initialize pygame, settings and screen object
	pygame.init()
	game_settings=Settings()
	screen=pygame.display.set_mode((game_settings.screen_width,game_settings.screen_height))
	pygame.display.set_caption("PONG!")
	
	rpaddle=Rpaddle(game_settings,screen)
	lpaddle=Lpaddle(game_settings,screen)
	ball=Ball(game_settings,screen)
	play_button=Button(screen,"Play")
	stats=Stats()
	scoreboard=Scoreboard(game_settings,screen,stats)
	winner_msg=Winnermsg(game_settings,screen)
	
	#start main loop
	while True:
		
		#watch for keyboard and mouse events
		gf.check_events(rpaddle,lpaddle,stats)
		if stats.game_active:
			gf.update_rpaddle(game_settings,rpaddle)
			gf.update_lpaddle(game_settings,lpaddle)
			gf.update_ball(game_settings,rpaddle,lpaddle,ball,stats,scoreboard,winner_msg)
		
		#update screen
		gf.update_screen(game_settings,screen,rpaddle,lpaddle,ball,play_button,stats,scoreboard,winner_msg)
		
run_game()
