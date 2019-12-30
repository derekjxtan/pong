import pygame
from pygame.sprite import Sprite

class Rpaddle(Sprite):
	"""class to manage the right paddle"""
	
	def __init__(self,game_settings,screen):
		"""create right paddle at right side of screen"""
		super(Rpaddle,self).__init__()
		self.screen=screen
		self.screen_rect=screen.get_rect()
		
		#create right paddle at (0,0) and the set correct position
		self.rect=pygame.Rect(0,0,game_settings.rpaddle_width,game_settings.rpaddle_height)
		self.rect.centery=self.screen_rect.centery
		self.rect.right=self.screen_rect.right-10
		
		#right paddle colour
		self.colour=game_settings.rpaddle_colour
		
		#store decimal for right paddle position
		self.center=float(self.rect.centery)
		
		#movement flag
		self.move_up=False
		self.move_down=False
		
	def update(self,game_settings):
		"""manage movement of right paddle"""
		if self.move_up and self.rect.top>0:
			self.center-=game_settings.rpaddle_speed_factor
		if self.move_down and self.rect.bottom<self.screen_rect.bottom:
			self.center+=game_settings.rpaddle_speed_factor
			
		self.rect.centery=self.center
		
	def draw_rpaddle(self):
		"""draw right paddle to screen"""
		pygame.draw.rect(self.screen,self.colour,self.rect)
		
