class Settings:
	"""All the settings for the game"""

	def __init__(self):
		"""initialise the game settings"""

		#screen settings
		self.screen_height = 800
		self.screen_width = 1200
		self.bg_color = (230, 230, 230)

		#ship settings
		self.ship_speed = 1.5
		self.ship_limit = 3

		#bullet settings
		self.bullet_speed = 1.0
		self.bullet_width = 3000
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)
		self.bullets_allowed = 3

		#alien settings
		self.alien_speed = 1.0
		self.fleet_drop_speed = 10
		#fleet_direction of 1 represents right and -1 represents left
		self.fleet_direction = 1
