def rook_possible_moves(self):
   poss_moves = []

   up_moves = list(map(lambda x: self.letter_coord + x, [str(x) for x in range(int(self.num_coord)+1, 9)]))
   right_moves = list(map(lambda x: x + self.num_coord, [chr(x) for x in range(ord(self.letter_coord)+1, 105)]))
   down_moves = list(map(lambda x: self.letter_coord + x, [str(x) for x in range(1, int(self.num_coord))]))
   left_moves = list(map(lambda x: x + self.num_coord, [chr(x) for x in range(97, ord(self.letter_coord))]))
   down_moves.reverse()
   left_moves.reverse()
   poss_moves.append(up_moves)
   poss_moves.append(right_moves)
   poss_moves.append(down_moves)
   poss_moves.append(left_moves)


   return poss_moves