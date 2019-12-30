import pygame.font

class Winnermsg():
	"""manage message to indicate winner"""
	
	def __init__(self,game_settings,screen):
		"""initialize attributes"""
		self.screen=screen
		self.screen_rect=screen.get_rect()
		self.game_settings=game_settings

		#properties
		self.msg_colour=(255,255,255)
		self.msg_font=pygame.font.SysFont(None,48)
		
		self.prep_rpaddle_msg()
		self.prep_lpaddle_msg()
		
	def prep_rpaddle_msg(self):
		#prepare message
		rpaddle_msg="The Winner is Right Player!" 
		self.rpaddle_msg_image=self.msg_font.render(rpaddle_msg,True,self.msg_colour,self.game_settings.bg_colour)
		
		#display msg in center top
		self.rpaddle_msg_rect=self.rpaddle_msg_image.get_rect()
		self.rpaddle_msg_rect.top=20
		self.rpaddle_msg_rect.centerx=self.screen_rect.centerx
	
	def prep_lpaddle_msg(self):
		#prepare message
		lpaddle_msg="The winner is Left Player!"
		self.lpaddle_msg_image=self.msg_font.render(lpaddle_msg,True,self.msg_colour,self.game_settings.bg_colour)
		
		#display msg in center top
		self.lpaddle_msg_rect=self.lpaddle_msg_image.get_rect()
		self.lpaddle_msg_rect.top=20
		self.lpaddle_msg_rect.centerx=self.screen_rect.centerx	
		
	def display_rpaddle_msg(self):
		#display message on screen
		self.screen.blit(self.rpaddle_msg_image,self.rpaddle_msg_rect)
		
	def display_lpaddle_msg(self):
		#display message on screen
		self.screen.blit(self.lpaddle_msg_image,self.lpaddle_msg_rect)
