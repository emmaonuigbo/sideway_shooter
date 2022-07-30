import pygame

class Ship:
	"""A class to manage the ship."""

	def __init__(self, ss_shooter):
		"""Initialize the ship and set its starting position."""
		self.screen = ss_shooter.screen
		self.settings = ss_shooter.settings
		self.screen_rect = ss_shooter.screen.get_rect()

		#Load the ship image and get its rect.
		self.image = pygame.image.load('ship.bmp')
		self.rect = self.image.get_rect()

		# Start each new ship at the left center of the screen.
		self.rect.midleft = self.screen_rect.midleft

		# Store a decimal value for the ship's horizontal position.
		self.y = float(self.rect.y)

		# Movement flags
		self.moving_down = False
		self.moving_up = False

	def update(self):
		"""Update the ship's position based on the movement flags."""
		# Update the ship's y value, not the rect.
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.rect.y += self.settings.ship_speed
		if self.moving_up and self.rect.top > 0:
			self.rect.y -= self.settings.ship_speed

		# Update rect object from self.y.

	def blitme(self):
		"""Draw the ship at its current location."""
		self.screen.blit(self.image, self.rect)