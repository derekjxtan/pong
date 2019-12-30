class Stats():
	"""manage all statistics in game"""
	
	def __init__(self):
		self.game_active=False
		
		self.initialize_scores()

	def initialize_scores(self):
		self.rpaddle_score=0
		self.lpaddle_score=0
