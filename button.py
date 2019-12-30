import pygame.font

class Button():
	
	def __init__(self,screen,msg):
		"""initialize button attributes"""
		self.screen=screen
		self.screen_rect=screen.get_rect()
		
		#set properties of button
		self.width=200
		self.height=50
		self.text_colour=(0,0,0)
		self.button_colour=(255,255,255)
		self.font=pygame.font.SysFont(None,48)
		
		#build button's rect and center it
		self.rect=pygame.Rect(0,0,self.width,self.height)
		self.rect.center=self.screen_rect.center
		
		#button message
		self.prep_msg(msg)
		
	def prep_msg(self,msg):
		"""turn msg into rendered image and center text on the button"""
		self.msg_image=self.font.render(msg,True,self.text_colour,self.button_colour)
		self.msg_image_rect=self.msg_image.get_rect()
		self.msg_image_rect.center=self.rect.center
		
	def draw_button(self):
		"""draw button to screen"""
		self.screen.fill(self.button_colour,self.rect)
		self.screen.blit(self.msg_image,self.msg_image_rect)
