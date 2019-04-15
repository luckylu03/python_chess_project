from pawn_move import *
from rook_move import *
from knight_move import *
from queen_move import *
from king_move import *

def figure_moves(Figure, field_coord, piece_info, begin_pos):

    if piece_info.type == 'P':
        piece_moves = pawn_possible_moves(piece_info, field_coord)
        # print(piece_moves)
    elif piece_info.type == 'R':
        piece_moves = rook_possible_moves(piece_info)
        # print(piece_moves)
    elif piece_info.type == 'Kn':
        piece_moves = knight_possible_moves(piece_info)
        print(piece_moves)
    elif piece_info.type == 'B':
        piece_moves = bishop_possible_moves(piece_info)
        # print(piece_moves)
    elif piece_info.type == 'Q':
        piece_moves = queen_possible_moves(piece_info)
        # print(piece_moves)
    elif piece_info.type == 'K':
        piece_moves = king_possible_moves(piece_info)
        # print(piece_moves)
    return piece_moves

def figure_movement(field_coord, begin_pos, end_pos, end_point_status = 'neutral'):
    if end_point_status == 'neutral':
        field_coord[begin_pos[0]][int(begin_pos[1]) - 1], field_coord[end_pos[0]][int(end_pos[1]) - 1] = field_coord[end_pos[0]][int(end_pos[1]) - 1], field_coord[begin_pos[0]][int(begin_pos[1]) - 1]
    elif end_point_status == 'enemy':
        field_coord[end_pos[0]][int(end_pos[1]) - 1] = ''
        figure_movement(field_coord, begin_pos, end_pos)
    return field_coord

def double_check_and_move(field_coord, checking_line, begin_pos, end_pos):
    if 'block' in checking_line.values():
        block_val = list(checking_line.keys())[list(checking_line.values()).index('block')]
        # print(field_coord[block_val[0]][int(block_val[1])-1], 'blocks the way on "', block_val,'" :(')
    elif 'enemy' in checking_line.values():
        field_coord = figure_movement(field_coord, begin_pos, end_pos, 'enemy')
    else:
        field_coord = figure_movement(field_coord, begin_pos, end_pos)
    return field_coord
    