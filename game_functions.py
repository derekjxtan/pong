import sys
import pygame
from time import sleep
from right_paddle import Rpaddle
from left_paddle import Lpaddle
from ball import Ball
from stats import Stats

def check_events(rpaddle,lpaddle,stats):
	"""respond to key presses"""
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			sys.exit()
			
		elif event.type==pygame.KEYDOWN:
			check_keydown_events(event,rpaddle,lpaddle,stats)
		
		elif event.type==pygame.KEYUP:
			check_keyup_events(event,rpaddle,lpaddle)

				
def check_keydown_events(event,rpaddle,lpaddle,stats):
	"""respond to key presses"""
	if event.key==pygame.K_q:
		sys.exit()
	if event.key==pygame.K_UP:
		#move right paddle up
		rpaddle.move_up=True
	if event.key==pygame.K_DOWN:
		#move right paddle down
		rpaddle.move_down=True
	if event.key==pygame.K_w:
		#move left paddle up
		lpaddle.move_up=True
	if event.key==pygame.K_s:
		#move left paddle down
		lpaddle.move_down=True
	if event.key==pygame.K_p:
		stats.game_active=True
		
def check_keyup_events(event,rpaddle,lpaddle):
	"""respond to key releases"""
	if event.key==pygame.K_UP:
		rpaddle.move_up=False
	if event.key==pygame.K_DOWN:
		rpaddle.move_down=False
	if event.key==pygame.K_w:
		lpaddle.move_up=False
	if event.key==pygame.K_s:
		lpaddle.move_down=False


def update_screen(game_settings,screen,rpaddle,lpaddle,ball,play_button,stats,scoreboard,winner_msg):
	"""update items on screen and flip to new screen"""
	#redraw screen through each loop
	screen.fill(game_settings.bg_colour)
	rpaddle.draw_rpaddle()
	lpaddle.draw_lpaddle()
	ball.draw_ball()
	scoreboard.draw_rpaddle_score()
	scoreboard.draw_lpaddle_score()
	if not stats.game_active:
		play_button.draw_button()
	if stats.rpaddle_score==5:
		winner_msg.display_rpaddle_msg()
	if stats.lpaddle_score==5:
		winner_msg.display_lpaddle_msg()
	
	#flip to latest screen
	pygame.display.flip()
	
def check_top_edge_collision(game_settings,ball):
	"""check for ball collision with edge and change y direction"""
	if ball.check_top_edges():
		change_y_direction(game_settings)
	
def change_y_direction(game_settings):
	game_settings.ball_directiony*=-1
	
def check_paddle_collision(game_settings,rpaddle,lpaddle,ball):
	"""check for collision with side edges"""
	if check_paddle(rpaddle,lpaddle,ball):
		change_x_direction(game_settings)
		if game_settings.ball_speed_factorx<=2 and game_settings.ball_speed_factory<=2:
			game_settings.increase_speed()
		
def check_paddle(rpaddle,lpaddle,ball):
	if pygame.sprite.collide_rect(rpaddle,ball):
		return True
	if pygame.sprite.collide_rect(lpaddle,ball):
		return True
	
def change_x_direction(game_settings):
	game_settings.ball_directionx*=-1
	
def check_rside_edge_collision(game_settings,ball,stats,scoreboard):
	if ball.check_rside_edge():
		ball.center_ball()
		sleep(0.5)
		game_settings.initialize_dynamic_settings()
		stats.lpaddle_score+=1
		scoreboard.prep_lpaddle_score(stats)
			
		
def check_lside_edge_collision(game_settings,ball,stats,scoreboard):
	if ball.check_lside_edge():
		ball.center_ball()
		sleep(0.5)
		game_settings.initialize_dynamic_settings()
		stats.rpaddle_score+=1
		scoreboard.prep_rpaddle_score(stats)
		
def end_game(game_settings,ball,stats,scoreboard,winner_msg):
	"""end the game if either side's score is 5"""
	if stats.rpaddle_score==5:
		stats.game_active=False
		game_settings.initialize_dynamic_settings()
		scoreboard.prep_lpaddle_score(stats)
		scoreboard.prep_rpaddle_score(stats)
		scoreboard.draw_lpaddle_score()
		scoreboard.draw_rpaddle_score()
		winner_msg.prep_rpaddle_msg()
		ball.center_ball()
		stats.initialize_scores()
	if stats.lpaddle_score==5:
		stats.game_active=False
		game_settings.initialize_dynamic_settings()
		scoreboard.prep_lpaddle_score(stats)
		scoreboard.prep_rpaddle_score(stats)
		scoreboard.draw_lpaddle_score()
		scoreboard.draw_rpaddle_score()
		winner_msg.prep_lpaddle_msg()
		ball.center_ball()
		stats.initialize_scores()
	
def update_ball(game_settings,rpaddle,lpaddle,ball,stats,scoreboard,winner_msg):
	check_top_edge_collision(game_settings,ball)
	check_paddle_collision(game_settings,rpaddle,lpaddle,ball)
	check_lside_edge_collision(game_settings,ball,stats,scoreboard)
	check_rside_edge_collision(game_settings,ball,stats,scoreboard)
	end_game(game_settings,ball,stats,scoreboard,winner_msg)
	ball.update(game_settings)
	
def update_rpaddle(game_settings,rpaddle):
	rpaddle.update(game_settings)
	
def update_lpaddle(game_settings,lpaddle):
	lpaddle.update(game_settings)
