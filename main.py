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

mouse_pos = [screen_width, screen_height]

while running:
    
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        
        if e.type == pygame.MOUSEBUTTONUP:
          mouse_pos = pygame.mouse.get_pos()

    screen.blit(background, (0, 0))

    # board
    j = 0
    while j<8:
        board_left = 32
        for i in range(0, 8, 2):
          field = pygame.Rect(board_left, board_top, field_size, field_size)
          mouse_rect = pygame.Rect(mouse_pos[0], mouse_pos[1], 1, 1)
          if field.contains(mouse_rect):
            mouse_pos = [j, i]
            print(mouse_pos)
          if board.board[j][i]:
            if board.board[j][i].selected:
              field_color = '#822C20'
            else:
              field_color = red
          else:
            field_color = red
          pygame.draw.rect(screen, field_color, field)
          board_left += field_size*2

        j+=1
        board_top += field_size
        board_left = 32 + field_size
        for i in range(1, 8, 2):
          field = pygame.Rect(board_left, board_top, field_size, field_size)
          mouse_rect = pygame.Rect(mouse_pos[0], mouse_pos[1], 1, 1)
          if field.contains(mouse_rect):
            mouse_pos = [j, i]
            print(mouse_pos)
          if board.board[j][i]:
            if board.board[j][i].selected:
              field_color = '#822C20'
            else:
              field_color = red
          else:
            field_color = red
          pygame.draw.rect(screen, field_color, field)
          board_left += field_size*2
        j+=1
        board_top += field_size
    
    board_left = 32
    board_top = 80

    j = 0
    while j<8:
        board_left = 32+field_size
        for i in range(1, 8, 2):
          field = pygame.Rect(board_left, board_top, field_size, field_size)
          mouse_rect = pygame.Rect(mouse_pos[0], mouse_pos[1], 1, 1)
          if field.contains(mouse_rect):
            mouse_pos = [j, i]
            print(mouse_pos)
          if board.board[j][i]:
            if board.board[j][i].selected:
              field_color = '#887F9D'
            else:
              field_color = navy_blue
          else:
            field_color = navy_blue
          pygame.draw.rect(screen, field_color, field)
          board_left += field_size*2

        j+=1
        board_top += field_size
        board_left = 32
        for i in range(0, 8, 2):
          field = pygame.Rect(board_left, board_top, field_size, field_size)
          mouse_rect = pygame.Rect(mouse_pos[0], mouse_pos[1], 1, 1)
          if field.contains(mouse_rect):
            mouse_pos = [j, i]
            print(mouse_pos)
          if board.board[j][i]:
            if board.board[j][i].selected:
              field_color = '#887F9D'
            else:
              field_color = navy_blue
          else:
            field_color = navy_blue
          pygame.draw.rect(screen, field_color, field)
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
            
            if [i, j] == mouse_pos:
              board.board[i][j].selected = True
            else:
              board.board[i][j].selected = False
              
    '''
    for i in range(8):
      for j in range(8):
        if [i, j] == mouse_pos:
          board.board[i][j].selected = True
        elif board.board[i][j]:
          board.board[i][j].selected = False
        '''      

    pygame.display.flip()
    clock.tick(60)

pygame.quit()