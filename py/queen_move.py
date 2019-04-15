from bishop_move import *
from rook_move import *

def queen_possible_moves(self):
   poss_moves = []
   poss_moves += (bishop_possible_moves(self))
   poss_moves += rook_possible_moves(self)
   return poss_moves