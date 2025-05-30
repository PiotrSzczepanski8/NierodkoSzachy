from board import *
import pygame

board = Board()

screen_width = 875
screen_height = 738

pygame.init()
pygame.display.set_caption('NierodkoSzachy')
title = 'NierodkoSzachy'

font = pygame.font.Font("fonts/DelaGothicOne.ttf", 36)
title_surface = font.render(title, True, "#000000")
title_rect = title_surface.get_rect()
title_rect.center = ((32 + 64*8) / 2, 40)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_icon(pygame.image.load('images/king.png'))

navy_blue = '#12003D'
red = '#E73A23'

clock = pygame.time.Clock()
running = True
game_active = False

board_top = 80
board_left = 32
field_size = 64

background = pygame.image.load('images/n-background.png')
background = pygame.transform.scale(background, (screen_width, screen_height))

mouse_pos = [screen_width, screen_height]

red_move = True
isTimeout = False

while running:
  
    if isTimeout:
        timeout+=1
    
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        
        if e.type == pygame.MOUSEBUTTONUP:
          mouse_pos = pygame.mouse.get_pos()
    
    screen.blit(background, (0, 0))
    screen.blit(title_surface, title_rect)
    
    '''
    if game_active == False:
      pygame.display.flip()
      clock.tick(60)
      continue
    '''

    # board
    j = 0
    while j<8:
        board_left = 32
        for i in range(0, 8, 2):
          field = pygame.Rect(board_left, board_top, field_size, field_size)
          mouse_rect = pygame.Rect(mouse_pos[0], mouse_pos[1], 1, 1)
          if red_move == False:
            draw_i = 7-i
            draw_j = 7-j
          else:
            draw_i = i
            draw_j = j
          if field.contains(mouse_rect):
            mouse_pos = [draw_j, draw_i]
            # print(mouse_pos)
          if board.board[draw_j][draw_i]:
            if board.board[draw_j][draw_i].selected:
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
          if red_move == False:
            draw_i = 7-i
            draw_j = 7-j
          else:
            draw_i = i
            draw_j = j
          if field.contains(mouse_rect):
            mouse_pos = [draw_j, draw_i]
            # print(mouse_pos)
          if board.board[draw_j][draw_i]:
            if board.board[draw_j][draw_i].selected:
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
          if red_move == False:
            draw_i = 7-i
            draw_j = 7-j
          else:
            draw_i = i
            draw_j = j
          if field.contains(mouse_rect):
            mouse_pos = [draw_j, draw_i]
            # print(mouse_pos)
          if board.board[draw_j][draw_i]:
            if board.board[draw_j][draw_i].selected:
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
          if red_move == False:
            draw_i = 7-i
            draw_j = 7-j
          else:
            draw_i = i
            draw_j = j
          if field.contains(mouse_rect):
            mouse_pos = [draw_j, draw_i]
            # print(mouse_pos)
          if board.board[draw_j][draw_i]:
            if board.board[draw_j][draw_i].selected:
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

    field_selected = False

    # pieces
    for i in range(8):
       for j in range(8):            
          if board.board[i][j]:
            
            image_name = 'images/' + board.board[i][j].name + '.png'

            if board.board[i][j].color == 'white':
                image_name = 'images/' + board.board[i][j].name + '-red.png'

            image = pygame.image.load(image_name)
            image = pygame.transform.scale(image, (field_size, field_size))
            
            if red_move == False:
              screen.blit(image, (board_left+(field_size*(7-j)), board_top+(field_size*(7-i))))
            else:
              screen.blit(image, (board_left+(field_size*j), board_top+(field_size*i)))
            
            if board.board[i][j].selected:
              field_selected = True
              selected_field = [i, j]

            if [i, j] == mouse_pos:
              if ((red_move and board.board[i][j].color == 'white') or (red_move == False and board.board[i][j].color == 'black')):
                board.board[i][j].selected = True
            else:
              board.board[i][j].selected = False
    
    if field_selected and mouse_pos[0] < 8 and mouse_pos[1] < 8:
      movement_allowed = board.board[selected_field[0]][selected_field[1]].check_movement(selected_field[0], selected_field[1], mouse_pos[0], mouse_pos[1])
      if board.board[mouse_pos[0]][mouse_pos[1]]:
        if board.board[selected_field[0]][selected_field[1]].color != board.board[mouse_pos[0]][mouse_pos[1]].color:
          different_color = True
        else:
          different_color = False
      else:
        different_color = True
        
      if board.board[selected_field[0]][selected_field[1]].name == 'pawn':
          if board.board[mouse_pos[0]][mouse_pos[1]]:
            movement_allowed = False
          color = board.board[selected_field[0]][selected_field[1]].color
          direction = -1 if color == 'white' else 1

          target_i, target_j = mouse_pos

          i, j = selected_field

          if target_i == i + direction and abs(target_j - j) == 1:
              target_piece = board.board[target_i][target_j]
              if target_piece and target_piece.color != color:
                  movement_allowed = True
            
      if board.board[selected_field[0]][selected_field[1]].name != 'knight' and movement_allowed:
        no_collision = board.no_collision(selected_field[0], selected_field[1], mouse_pos[0], mouse_pos[1])
        # print(no_collision)
      else:
        no_collision = True
      # print(movement_allowed)
    
      if movement_allowed and mouse_pos != selected_field and different_color and no_collision:
        board.board[mouse_pos[0]][mouse_pos[1]] = board.board[selected_field[0]][selected_field[1]]
        board.board[mouse_pos[0]][mouse_pos[1]].selected = False
        board.board[selected_field[0]][selected_field[1]] = None
        '''
        if red_move:
            red_move = False
        else:
            red_move = True
        '''
        isTimeout = True
        timeout = 0
           
    
    
    if isTimeout and timeout == 20:  
          isTimeout = False
          for i in range(8):
            for j in range(8):
              if board.board[i][j]:
                board.board[i][j].selected = False
          if red_move:
            red_move = False
          else:
            red_move = True
    
            
    pygame.display.flip()
    clock.tick(60)

pygame.quit()