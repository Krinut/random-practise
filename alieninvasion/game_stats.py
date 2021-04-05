class GameStats:
	"""Track statistics of the game"""

	def __init__(self, ai_game):
		"""initialise statistics"""
		self.settings = ai_game.settings
		self.reset_stats()
		self.game_active = False

	def reset_stats(self):
		"""initialise statistics that can change during the game"""
		self.ships_left = self.settings.ship_limit
