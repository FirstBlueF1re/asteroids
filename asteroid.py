import pygame
import random
from logger import log_event
from circleshape import CircleShape
from constants import PLAYER_RADIUS, LINE_WIDTH, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)

	def draw(self, screen):
		pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

	def update(self, dt):
		self.position += (self.velocity * dt)

	def split(self):
		self.kill()
		if self.radius <= ASTEROID_MIN_RADIUS:
			return
		else:
			log_event("asteroid_split")
			rando_angle1 = random.uniform(20, 50)
			rando_angle2 = -rando_angle1
			new_vec_1= self.velocity.rotate(rando_angle1)
			new_vec_2 = self.velocity.rotate(rando_angle2)
			new_radius = self.radius - ASTEROID_MIN_RADIUS
			first_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
			second_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
			first_asteroid.velocity = new_vec_1 * 1.2
			second_asteroid.velocity = new_vec_2 * 1.2
