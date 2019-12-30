from random import randint

class Settings():
	"""class to store all settings for game"""
	
	def __init__(self):
		"""initialize static settings"""
		#screen settings
		self.screen_width=1200
		self.screen_height=600
		self.bg_colour=(0,0,0)
		
		#right paddle settings
		self.rpaddle_speed_factor=2
		self.rpaddle_width=5
		self.rpaddle_height=100
		self.rpaddle_colour=(255,255,255)
		
		#left paddle settings
		self.lpaddle_speed_factor=2
		self.lpaddle_width=5
		self.lpaddle_height=100
		self.lpaddle_colour=(255,255,255)
		
		#ball settings
		self.ball_directionx=1
		self.ball_directiony=1
		self.ball_width=10
		self.ball_height=10
		self.ball_colour=(255,255,255)
		
		#speed up scale
		self.speed_up=1.05
		
		self.initialize_dynamic_settings()
		
	def initialize_dynamic_settings(self):
		"""initialize settings that change throughout game"""
		self.ball_speed_factorx=randint(5,10)*0.1
		self.ball_speed_factory=randint(5,10)*0.1
		
	def increase_speed(self):
		"""increase speed of ball"""
		self.ball_speed_factorx*=self.speed_up
		self.ball_speed_factory*=self.speed_up
