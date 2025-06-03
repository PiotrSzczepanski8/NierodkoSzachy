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

promotion = False
promotion_pieces = ["bishop", "rook", "queen", "knight"]
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
    
    if promotion:
      dialog_left = 560
      if red_move:
        piece_color = "red"
      else:
        piece_color = ""

      for piece in promotion_pieces:
        if piece_color == "":
          image_name = "images/" + piece + ".png"
        else:
          image_name = "images/" + piece + "-" + piece_color + ".png"
        image = pygame.image.load(image_name)
        image = pygame.transform.scale(image, (field_size, field_size))
        screen.blit(image, (dialog_left, 150))
        
        field = pygame.Rect(dialog_left, 150, field_size, field_size)
        mouse_rect = pygame.Rect(mouse_pos[0], mouse_pos[1], 1, 1)
        
        if field.contains(mouse_rect):
          promotion = False
          timeout = 0
          board.board[promotion_y, promotion_x].name = piece
 
        dialog_left += 74
            
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
            print(mouse_pos)
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
            print(mouse_pos)
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
            print(mouse_pos)
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
            print(mouse_pos)
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
      castling = False
      if board.board[selected_field[0]][selected_field[1]].name == 'king':
          if board.board[selected_field[0]][selected_field[1]].has_moved == False:
            if mouse_pos[0] == 7 and mouse_pos[1] == 6:
                if board.board[7][7]:
                  if board.board[7][7].has_moved == False and board.board[7][7].name == 'rook':
                    castling = True
                    board.board[mouse_pos[0]][mouse_pos[1]] = board.board[selected_field[0]][selected_field[1]]
                    board.board[mouse_pos[0]][mouse_pos[1]].selected = False
                    board.board[mouse_pos[0]][mouse_pos[1]].has_moved = True
                    board.board[selected_field[0]][selected_field[1]] = None
                    board.board[7][5] = board.board[7][7]
                    board.board[7][5].has_moved = True
                    board.board[7][7] = None
                    isTimeout = True
                    timeout = 0
            
            if mouse_pos[0] == 7 and mouse_pos[1] == 2:
              if board.board[7][0]:
                  if board.board[7][0].has_moved == False and board.board[7][0].name == 'rook':
                      if board.board[7][1] is None and board.board[7][2] is None and board.board[7][3] is None:
                          castling = True
                          board.board[7][2] = board.board[7][4]
                          board.board[7][2].selected = False
                          board.board[7][2].has_moved = True
                          board.board[7][4] = None
                          board.board[7][3] = board.board[7][0]
                          board.board[7][3].has_moved = True
                          board.board[7][0] = None
                          isTimeout = True
                          timeout = 0
                          
            if mouse_pos[0] == 0 and mouse_pos[1] == 6:
              if board.board[0][7]:
                  if board.board[0][7].has_moved == False and board.board[0][7].name == 'rook':
                      if board.board[0][5] is None and board.board[0][6] is None:
                          castling = True
                          board.board[0][6] = board.board[0][4]
                          board.board[0][6].selected = False
                          board.board[0][6].has_moved = True
                          board.board[0][4] = None
                          board.board[0][5] = board.board[0][7]
                          board.board[0][5].has_moved = True
                          board.board[0][7] = None
                          isTimeout = True
                          timeout = 0
                          
            if mouse_pos[0] == 0 and mouse_pos[1] == 2:
              if board.board[0][0]:
                  if board.board[0][0].has_moved == False and board.board[0][0].name == 'rook':
                      if board.board[0][1] is None and board.board[0][2] is None and board.board[0][3] is None:
                          castling = True
                          board.board[0][2] = board.board[0][4]
                          board.board[0][2].selected = False
                          board.board[0][2].has_moved = True
                          board.board[0][4] = None
                          board.board[0][3] = board.board[0][0]
                          board.board[0][3].has_moved = True
                          board.board[0][0] = None
                          isTimeout = True
                          timeout = 0


      
      if board.board[selected_field[0]][selected_field[1]] and board.board[selected_field[0]][selected_field[1]].name != 'knight' and movement_allowed:
        no_collision = board.no_collision(selected_field[0], selected_field[1], mouse_pos[0], mouse_pos[1])
      else:
        no_collision = True
      if promotion:
        movement_allowed = False
        
      if movement_allowed and mouse_pos != selected_field and different_color and no_collision and not castling:
        board.board[mouse_pos[0]][mouse_pos[1]] = board.board[selected_field[0]][selected_field[1]]
        if board.board[selected_field[0]][selected_field[1]].name == "pawn":
            if mouse_pos[0] == 0 or mouse_pos[0] == 7:
              promotion = True
              promotion_x = mouse_pos[1]
              promotion_y = mouse_pos[0]
        board.board[mouse_pos[0]][mouse_pos[1]].selected = False
        board.board[selected_field[0]][selected_field[1]] = None
        isTimeout = True
        timeout = 0
           
    
    
    if isTimeout and timeout == 20 and not promotion:  
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