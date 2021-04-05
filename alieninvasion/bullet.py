import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""A class to defin the bullets"""

	def __init__(self, ai_game):
		"""create a bullet object at ship's current location"""
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.color = self.settings.bullet_color

		#create a bullet rect at (0,0) and then set it correct location.
		self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
		self.rect.midtop = ai_game.ship.rect.midtop

		#store bullet's position as decimal value
		self.y = float(self.rect.y)

	def update(self):
		"""move the bullet up the screen"""
		#update decimal value of bullet
		self.y -= self.settings.bullet_speed
		#update rect position
		self.rect.y = self.y

	def draw_bullet(self):
		"""Draw the bullet to the screen"""
		pygame.draw.rect(self.screen, self.color, self.rect)
