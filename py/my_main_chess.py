import copy
from board_coord_gen import *
from figure_moves import figure_moves, double_check_and_move
from line_check import line_check
from is_checked import checked_or_not, under_check
from all_possibilities import *


begin_pos = ''
last_move_color = 'B'
moves_to_cover = []

class Figure:
   def __init__(self, letter = 'a', num = '2', color = '', fig_type = ''):
      self.color = color
      self.type = fig_type
      self.letter_coord = letter
      self.num_coord = num


field_coord = coord_gen()

while begin_pos != 'exit':

   print(int(32/8), 32%8)

   begin_pos = input("Enter begin_pos: ")

   if field_coord[begin_pos[0]][int(begin_pos[1])-1][0] == last_move_color:
      while field_coord[begin_pos[0]][int(begin_pos[1])-1][0] == last_move_color:
         print('Another side to move')
         begin_pos = input("Enter begin_pos: ")
      else:
         if field_coord[begin_pos[0]][int(begin_pos[1]) - 1] == '': 
            print(1)
         else:
            piece_info = field_coord[begin_pos[0]][int(begin_pos[1]) - 1] + begin_pos
            piece_info = Figure(begin_pos[0], begin_pos[1], piece_info[0], piece_info[1:-2])
   if field_coord[begin_pos[0]][int(begin_pos[1])-1][0] != last_move_color:
      print('We are good')
      if field_coord[begin_pos[0]][int(begin_pos[1]) - 1] == '': 
         print(1)
      else:
         piece_info = field_coord[begin_pos[0]][int(begin_pos[1]) - 1] + begin_pos
         piece_info = Figure(begin_pos[0], begin_pos[1], piece_info[0], piece_info[1:-2])

   piece_moves = figure_moves(Figure, field_coord, piece_info, begin_pos)

   end_pos = input("Enter end_pos: ")
   
   checking_line = line_check(field_coord, end_pos, piece_moves, last_move_color)

   print(checking_line)
   piece_info.letter_coord = end_pos[0]
   piece_info.num_coord = end_pos [1]
   piece_moves = figure_moves(Figure, field_coord, piece_info, end_pos)

   field_coord_copy = copy.deepcopy(field_coord)
   field_coord = double_check_and_move(field_coord, checking_line, begin_pos, end_pos)

   if field_coord_copy == field_coord:
      pass
   else:
      last_move_color = piece_info.color

   defence_piece = Figure()
   attack_piece = Figure()

   piece_check_info = position_check_for_checks(Figure, attack_piece, field_coord, begin_pos, last_move_color)
   if piece_check_info:
      moves_to_cover = check_escape_try(Figure, field_coord, defence_piece, attack_piece, begin_pos, last_move_color)
      if moves_to_cover:
         print(moves_to_cover)
      else:
         print('checkmate')

   print(field_coord['a'])
   print(field_coord['b'])
   print(field_coord['c'])
   print(field_coord['d'])
   print(field_coord['e'])
   print(field_coord['f'])
   print(field_coord['g'])
   print(field_coord['h'])