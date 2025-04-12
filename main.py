from board import *
import pygame

board = Board()
board.setup_pieces()

pygame.init()

screen_width = 875
screen_height = 738

screen = pygame.display.set_mode((screen_width, screen_height))

navy_blue = '#12003D'
red = '#E73A23'

clock = pygame.time.Clock()
running = True

board_top = 80
board_left = 32
field_size = 64

background = pygame.image.load('images/n-background.png')
background = pygame.transform.scale(background, (screen_width, screen_height))

while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))
    board_top = 80

    pygame.draw.rect(screen, red, pygame.Rect(board_left, board_top, field_size*8, field_size*8))

    j = 0
    while j<8:
        board_left = 32+field_size
        for i in range(4):
          pygame.draw.rect(screen, navy_blue, pygame.Rect(board_left, board_top, field_size, field_size))
          board_left += field_size*2

        j+=1
        board_top += field_size
        board_left = 32
        for i in range(4):
          pygame.draw.rect(screen, navy_blue, pygame.Rect(board_left, board_top, field_size, field_size))
          board_left += field_size*2
        j+=1
        board_top += field_size
    
    board_left = 32

    pygame.display.flip()
    clock.tick(60)

pygame.quit()