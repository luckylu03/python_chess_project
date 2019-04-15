def bishop_possible_moves(self):
   poss_moves = []
   up_left_moves = []
   up_right_moves = []
   down_right_moves = []
   down_left_moves = []
   
   if self.letter_coord == 'a' or int(self.num_coord) == 8:
      pass
   else:
      i = 1
      board_letter = ord(self.letter_coord)
      board_num = int(self.num_coord)
      while board_letter > ord('a') and board_letter <= ord('h') and board_num >= 1 and board_num < 8:
         up_left_moves.append(chr(ord(self.letter_coord)-i) + str(int(self.num_coord)+i))
         board_letter = ord(self.letter_coord)-i
         board_num = int(self.num_coord)+i
         i += 1

   if self.letter_coord == 'h' or int(self.num_coord) == 8:
      pass
   else:
      i = 1
      board_letter = ord(self.letter_coord)
      board_num = int(self.num_coord)
      while board_letter >= ord('a') and board_letter < ord('h') and board_num >= 1 and board_num < 8:
         up_right_moves.append(chr(ord(self.letter_coord)+i) + str(int(self.num_coord)+i))
         board_letter = ord(self.letter_coord)+i
         board_num = int(self.num_coord)+i
         i += 1

   if self.letter_coord == 'h' or int(self.num_coord) == 1:
      pass
   else:
      i = 1
      board_letter = ord(self.letter_coord)
      board_num = int(self.num_coord)
      while board_letter >= ord('a') and board_letter < ord('h') and board_num > 1 and board_num <= 8:
         down_right_moves.append(chr(ord(self.letter_coord)+i) + str(int(self.num_coord)-i))
         board_letter = ord(self.letter_coord)+i
         board_num = int(self.num_coord)-i
         i += 1

   if self.letter_coord == 'a' or int(self.num_coord) == 1:
      pass
   else:
      i = 1
      board_letter = ord(self.letter_coord)
      board_num = int(self.num_coord)
      while board_letter > ord('a') and board_letter <= ord('h') and board_num > 1 and board_num <= 8:
         down_left_moves.append(chr(ord(self.letter_coord)-i) + str(int(self.num_coord)-i))
         board_letter = ord(self.letter_coord)-i
         board_num = int(self.num_coord)-i
         i += 1

   poss_moves.append(up_left_moves)
   poss_moves.append(up_right_moves)
   poss_moves.append(down_right_moves)
   poss_moves.append(down_left_moves)

   return poss_moves