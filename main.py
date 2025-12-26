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
	log_state()
	#this is where the exit code would go for closing a window...if it worked...
	screen.fill("black")
	Player1.draw(screen)
	pygame.display.flip()
	dt = ( clock.tick(60) / 1000 )

def main():
	print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
	print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
	main()

