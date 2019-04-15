def pawn_possible_moves(self, field_coord):
      poss_moves = []
      if self.color == 'W':
         if field_coord[self.letter_coord][int(self.num_coord)] != '':
            pass
         else:
            poss_moves.append(self.letter_coord + str(int(self.num_coord) + 1))
         if self.letter_coord <= 'h' and self.letter_coord > 'a':
            if field_coord[chr(ord(self.letter_coord)-1)][int(self.num_coord)] != '':
               if field_coord[chr(ord(self.letter_coord)-1)][int(self.num_coord)][0] == 'B':
                  poss_moves.append(chr(ord(self.letter_coord)-1) + str(int(self.num_coord)+1))
         if self.letter_coord < 'h' and self.letter_coord >= 'a':
            if field_coord[chr(ord(self.letter_coord)+1)][int(self.num_coord)] != '':
               if field_coord[chr(ord(self.letter_coord)+1)][int(self.num_coord)][0] == 'B':
                  poss_moves.append(chr(ord(self.letter_coord)+1) + str(int(self.num_coord)+1))
         if int(self.num_coord) == 2 and field_coord[self.letter_coord][int(self.num_coord)] == '' and field_coord[self.letter_coord][int(self.num_coord)+1] == '':
            poss_moves.append(self.letter_coord + str(int(self.num_coord) + int(self.num_coord)))
      elif self.color == 'B':
         if field_coord[self.letter_coord][int(self.num_coord)-2] != '':
            pass
         else:
            poss_moves.append(self.letter_coord + str(int(self.num_coord) - 1))
         if self.letter_coord <= 'h' and self.letter_coord > 'a':
            if field_coord[chr(ord(self.letter_coord)-1)][int(self.num_coord) - 2] != '':
               if field_coord[chr(ord(self.letter_coord)-1)][int(self.num_coord) - 2][0] == 'W':
                  poss_moves.append(chr(ord(self.letter_coord)-1) + str(int(self.num_coord)-1))
         if self.letter_coord < 'h' and self.letter_coord >= 'a':
            if field_coord[chr(ord(self.letter_coord)+1)][int(self.num_coord) - 2] != '':
               if field_coord[chr(ord(self.letter_coord)+1)][int(self.num_coord) - 2][0] == 'W':
                  poss_moves.append(chr(ord(self.letter_coord)+1) + str(int(self.num_coord)-1))
         if int(self.num_coord) == 7 and field_coord[self.letter_coord][int(self.num_coord)-2] == '' and field_coord[self.letter_coord][int(self.num_coord)-3] == '':
            poss_moves.append(self.letter_coord + str(int(self.num_coord) - 2))
      return poss_moves