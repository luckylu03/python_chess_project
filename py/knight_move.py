def knight_possible_moves(self):
   poss_moves = []
   letter_left = []
   letter_right = []
   num_top = []
   num_bottom = []
   for i in range(1,3):
      letter_left.append(chr(ord(self.letter_coord)+i))
      letter_right.append(chr(ord(self.letter_coord)-i))
      num_top.append(str(int(self.num_coord)+i))
      num_bottom.append(str(int(self.num_coord)-i))

   if self.letter_coord == 'a' or int(self.num_coord) > 6:
      print(1)
   else:
      poss_moves.append(letter_right[0] + num_top[1])
   
   if self.letter_coord == 'h' or int(self.num_coord) > 6:
      print(2)
   else:
      poss_moves.append(letter_left[0] + num_top[1])
   
   if ord(self.letter_coord) > 102 or int(self.num_coord) == 8:
      print(3)
   else:
      poss_moves.append(letter_left[1] + num_top[0])
   
   if ord(self.letter_coord) > 103 or int(self.num_coord) == 1:
      print(4)
   else:
      poss_moves.append(letter_left[1] + num_bottom[0])
   
   if self.letter_coord == 'h' or int(self.num_coord) < 3:
      print(5)
   else:
      poss_moves.append(letter_left[0] + num_bottom[1])
   
   if self.letter_coord == 'a' or int(self.num_coord) < 3:
      print(6)
   else:
      poss_moves.append(letter_right[0] + num_bottom[1])

   if ord(self.letter_coord) < 99 or int(self.num_coord) == 1:
      print(7)
   else:
      poss_moves.append(letter_right[1] + num_bottom[0])

   if ord(self.letter_coord) < 99 or int(self.num_coord) == 8:
      print(8)
   else:
      poss_moves.append(letter_right[1] + num_top[0])
   
   return poss_moves