import pygame
import sys
from circleshape import CircleShape
from logger import log_event
from player import Player
from logger import log_state
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

#initialize pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
dt = 0
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()

Player.containers = (updatable, drawable)
Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = (updatable)
Shot.containers = (shots, updatable, drawable)

Player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
AsteroidField1 = AsteroidField()


while True:
	dt = (clock.tick(60) / 1000)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			raise SystemExit

	log_state()
	screen.fill("black")
	updatable.update(dt)
	for i in asteroids:
		if i.collides_with(Player1):
			log_event("player_hit")
			print("Game over!")
			sys.exit()
	for i in drawable:
		i.draw(screen)
	pygame.display.flip()

def main():
	print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
	print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
	main()

