import pygame.font

class Scoreboard():
	"""manage display of scores"""
	
	def __init__(self,game_settings,screen,stats):
		"""initialize attributes"""
		self.screen=screen
		self.screen_rect=screen.get_rect()
		self.stats=stats
		self.game_settings=game_settings
		
		#properties of rpaddle score
		self.rpaddle_score_colour=(255,255,255)
		self.rpaddle_font=pygame.font.SysFont(None,48)
		
		#properties of lpaddle score
		self.lpaddle_score_colour=(255,255,255)
		self.lpaddle_font=pygame.font.SysFont(None,48)
		
		#prep score
		self.prep_rpaddle_score(stats)
		self.prep_lpaddle_score(stats)

	def prep_rpaddle_score(self,stats):
		#prepare score 
		rpaddle_score_str=str(stats.rpaddle_score)
		self.rpaddle_score_image=self.rpaddle_font.render(rpaddle_score_str,True,self.rpaddle_score_colour,self.game_settings.bg_colour)
		
		#display score on top right corner
		self.rpaddle_score_image_rect=self.rpaddle_score_image.get_rect()
		self.rpaddle_score_image_rect.top=20
		self.rpaddle_score_image_rect.centerx=self.screen_rect.right-30
		
	def prep_lpaddle_score(self,stats):
		#prepare score
		lpaddle_score_str=str(stats.lpaddle_score)
		self.lpaddle_score_image=self.lpaddle_font.render(lpaddle_score_str,True,self.lpaddle_score_colour,self.game_settings.bg_colour)
		
		#display score on top left corner
		self.lpaddle_score_image_rect=self.lpaddle_score_image.get_rect()
		self.lpaddle_score_image_rect.top=20
		self.lpaddle_score_image_rect.centerx=30
	
	def draw_rpaddle_score(self):
		#draw right paddle score to screen
		self.screen.blit(self.rpaddle_score_image,self.rpaddle_score_image_rect)
		
	def draw_lpaddle_score(self):
		#draw left paddle_score to screen
		self.screen.blit(self.lpaddle_score_image,self.lpaddle_score_image_rect)
