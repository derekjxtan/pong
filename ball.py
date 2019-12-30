import pygame
from pygame.sprite import Sprite

class Ball:
	"""class to manage the ball"""
	
	def __init__(self,game_settings,screen):
		"""create ball and place in center of screen"""
		super(Ball,self).__init__
		self.screen=screen
		self.screen_rect=screen.get_rect()
		
		#create ball at (0,0) and place at correct position
		self.rect=pygame.Rect(0,0,game_settings.ball_width,game_settings.ball_height)
		self.rect.centerx=self.screen_rect.centerx
		self.rect.centery=self.screen_rect.centery
		
		#store decimal for ball position
		self.centerx=float(self.rect.centery)
		self.centery=float(self.rect.centery)
		
		#ball colour
		self.colour=game_settings.ball_colour
		
		#movement flag
		self.ball_move=True
		
	def update(self,game_settings):
		"""manage movement of ball"""
		if self.ball_move:
			self.centerx+=game_settings.ball_speed_factorx*game_settings.ball_directionx
			self.centery+=game_settings.ball_speed_factory*game_settings.ball_directiony
			
			
		self.rect.centerx=self.centerx
		self.rect.centery=self.centery
		
	def check_top_edges(self):
		"""check for collision with top and botton edge of screen"""
		if self.rect.top<=self.screen_rect.top:
			return True
		if self.rect.bottom>=self.screen_rect.bottom:
			return True

	def check_rside_edge(self):
		"""check for collision with right edge of screen"""
		if self.rect.right>=self.screen_rect.right:
			return True
	
	def check_lside_edge(self):
		"""check for collision with left edge of screen"""
		if self.rect.left<=self.screen_rect.left:
			return True
			
	def draw_ball(self):
		"""draw ball to screen"""
		pygame.draw.rect(self.screen,self.colour,self.rect)
		
	def center_ball(self):
		"""return ball to center location"""
		self.centerx=self.screen_rect.centerx
		self.centery=self.screen_rect.centery
