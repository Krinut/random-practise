import pygame

class Ship:
	"""A class to manage the ship"""

	def __init__(self, ai_game):
		"""initialise the ship and set its starting position"""
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.screen_rect = ai_game.screen.get_rect()
		self.moving_right = False	#movement flag for continous movement
		self.moving_left = False
		#load ship image and get its rect attributes
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()


		#start a new ship at the bottom mid of screen
		self.rect.midbottom = self.screen_rect.midbottom

		#store a decimal value for ship's horizontal position
		self.x = float(self.rect.x)

	def update(self):
		"""Update the position of ship based on movement flag"""
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += self.settings.ship_speed
		if self.moving_left and self.rect.left > 0:
			self.x -= self.settings.ship_speed

		#update rect object from self.x
		self.rect.x = self.x

	def center_ship(self):
		"""center the ship on the screen"""
		self.rect.midbottom = self.screen_rect.midbottom
		self.x = float(self.rect.x)

	def blitme(self):
		"""Draw the ship at its current location"""
		self.screen.blit(self.image, self.rect)
