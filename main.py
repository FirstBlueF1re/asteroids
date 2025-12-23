import pygame
from logger import log_state
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

#initialize pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

while True:
	log_state()
	#this is where the exit code would go for closing a window...if it worked...
	screen.fill("black")
	pygame.display.flip()

def main():
	print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
	print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
	main()

