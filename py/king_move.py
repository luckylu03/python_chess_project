def king_possible_moves(self):
   poss_moves = []
   up_moves = []
   right_moves = []
   down_moves = []
   left_moves = []
   coord_change = [-1, 0, 1]
   if int(self.num_coord) == 8:
      print(1)
   else:
      for j in range(3):
         up_moves.append(chr(ord (self.letter_coord) + coord_change[j]) + str(int(self.num_coord) + 1))

   if self.letter_coord == 'h':
      print(2)
   else:
      right_moves.append(chr(ord (self.letter_coord) + 1) + str(int(self.num_coord)))
   
   if int(self.num_coord) == 1:
      print(3)
   else:
      for j in range(3):
         down_moves.append(chr(ord (self.letter_coord) + coord_change[j]) + str(int(self.num_coord) -1))
   
   if self.letter_coord == 'a':
      print(4)
   else:
      left_moves.append(chr(ord (self.letter_coord) - 1) + str(int(self.num_coord)))
   for i in up_moves:
      poss_moves.append(i)
   for i in right_moves:
      poss_moves.append(i)
   for i in down_moves:
      poss_moves.append(i)
   for i in left_moves:
      poss_moves.append(i)
   return poss_moves