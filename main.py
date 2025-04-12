from board import *
import pygame

board = Board()

pygame.init()
pygame.display.set_caption('NierodkoSzachy')

screen_width = 875
screen_height = 738

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_icon(pygame.image.load('images/king.png'))

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

    pygame.draw.rect(screen, red, pygame.Rect(board_left, board_top, field_size*8, field_size*8))

    # board
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
    board_top = 80

    # pieces
    for i in range(8):
       for j in range(8):
          if board.board[i][j]:
            image_name = 'images/' + board.board[i][j].name + '.png'

            if board.board[i][j].color == 'white':
                image_name = 'images/' + board.board[i][j].name + '-red.png'
               
            image = pygame.image.load(image_name)
            image = pygame.transform.scale(image, (field_size, field_size))

            screen.blit(image, (board_left+(field_size*j), board_top+(field_size*i)))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()