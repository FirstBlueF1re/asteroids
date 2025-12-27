import pygame
from player import Player
from logger import log_state
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

#initialize pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
dt = 0
x = (SCREEN_WIDTH / 2)
y = (SCREEN_HEIGHT / 2)
Player1 = Player(x, y)

while True:
	dt = (clock.tick(60) / 1000)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			raise SystemExit

	log_state()
	screen.fill("black")
	Player1.update(dt)
	Player1.draw(screen)
	pygame.display.flip()

def main():
	print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
	print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
	main()

