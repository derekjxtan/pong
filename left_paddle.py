import pygame
from pygame.sprite import Sprite

class Lpaddle():
	"""class to manage left paddle"""
	
	def __init__(self,game_settings,screen):
		#create left paddle at left side of screen
		super(Lpaddle,self).__init__
		self.screen=screen
		self.screen_rect=screen.get_rect()
		
		#create left paddle at (0,0) and move to left side of screen
		self.rect=pygame.Rect(0,0,game_settings.lpaddle_width,game_settings.lpaddle_height)
		self.rect.centery=self.screen_rect.centery
		self.rect.centerx=10
		
		#left paddle colour
		self.colour=game_settings.lpaddle_colour
		
		#store decimal place for left paddle position
		self.center=float(self.rect.centery)
		
		#movement flag
		self.move_up=False
		self.move_down=False
		
	def update(self,game_settings):
		if self.move_up and self.rect.top>0:
			self.center-=game_settings.lpaddle_speed_factor
		if self.move_down and self.rect.bottom<self.screen_rect.bottom:
			self.center+=game_settings.lpaddle_speed_factor
		
		self.rect.centery=self.center
		
	def draw_lpaddle(self):
		"""draw left paddle to screen"""
		pygame.draw.rect(self.screen,self.colour,self.rect)	
