from line_check import *

def checked_or_not(checking_field, piece_pos):
    result = []

    if 'block' in checking_field.values() and 'check' in checking_field.values():
        block_vs_check = list(checking_field.keys())[list(checking_field.values()).index('block')]
        check_vs_block = list(checking_field.keys())[list(checking_field.values()).index('check')]
        if list(checking_field).index(check_vs_block) < list(checking_field).index(block_vs_check):
            # print('King is under atack')
            pos_giving_check = piece_pos
            result.append(pos_giving_check)
        else:
            pass
    elif 'check' in checking_field.values():
        check_vs_block = list(checking_field.keys())[list(checking_field.values()).index('check')]
        print('King is under atack')
        pos_giving_check = piece_pos
        result.append(pos_giving_check)
    return result

def under_check(Figure, field_coord, piece_moves, piece_pos, last_move_color):
    piece_check_info = []
    if len(piece_moves) == 0:
        pass
    elif isinstance(piece_moves[0], str):
        for i in piece_moves:
            checking_field = line_check(field_coord, i, piece_moves, last_move_color)
            check_info = checked_or_not(checking_field, piece_pos)
    else:
        for i in range(len(piece_moves)):
            if not piece_moves[i]:
                # print('No moves in this direction')
                pass
            else:
                checking_field = line_check(field_coord, piece_moves[i][-1], piece_moves, last_move_color)
                check_info = checked_or_not(checking_field, piece_pos)
                if check_info:
                    piece_check_info = check_info
    # if piece_check_info:
    #     print(checking_field)
    #     print(piece_check_info)
    return piece_check_info
    