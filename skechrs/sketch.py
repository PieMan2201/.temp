import pygame
pygame.init()

screen = pygame.display.set_mode((640,480))
s = pygame.Surface((300,210))
s.fill((222,222,222))
clock = pygame.time.Clock()
x = 150
y = 105

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			raise Exception
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
			why = 20
			while why > 0:
				screen.fill((255,0,255))
				screen.blit(bigger_s, (20,why))
				pygame.display.update()
				why = why - 1
				clock.tick(24)
			while why < 40:
				screen.fill((255,0,255))
				screen.blit(bigger_s, (20,why))
				pygame.display.flip()
				why = why + 1
				clock.tick(24)
			s.fill((222,222,222))
	keys = pygame.key.get_pressed()

	if keys[pygame.K_UP]:
		y = y - 1
	if keys[pygame.K_DOWN]:
		y = y + 1
	if keys[pygame.K_LEFT]:
		x = x - 1
	if keys[pygame.K_RIGHT]:
		x = x + 1

	if x < 0:
		x = 0
	if x > 299:
		x = 299
	if y < 0:
		y = 0
	if y > 209:
		y = 209

	screen.fill((255,0,255))
	s.set_at((x,y), pygame.Color(22,22,22))
	bigger_s = pygame.transform.scale(s, (600, 440))
	screen.blit(bigger_s, (20,20))
	pygame.display.flip()
	clock.tick(24)
