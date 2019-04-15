from figure_moves import figure_moves
from is_checked import under_check
from line_check import line_check
from figure_moves import double_check_and_move

def position_check_for_checks(Figure, attack_piece, field_coord, begin_pos, last_move_color):
    piece_check_info = []
    letter_of_line = 'a'
    for val in field_coord.values():
        for val2 in val:
            if val2 != '':
                if val2[0] == last_move_color and val2[1] != 'P' and val2[1:] != 'Kn' and val2[1] != 'K':
                    attack_piece.color = val2[0]
                    attack_piece.type = val2[1]
                    attack_piece.letter_coord = letter_of_line
                    attack_piece.num_coord = str(val.index(val2) + 1)
                    field_check = attack_piece.letter_coord + attack_piece.num_coord
                    piece_moves = figure_moves(Figure, field_coord, attack_piece, begin_pos)
                    piece_check_info += under_check(Figure, field_coord, piece_moves, field_check, last_move_color)
                elif val2[1:] == 'Kn':
                    attack_piece.color = val2[0]
                    attack_piece.type = val2[1]
                    attack_piece.letter_coord = letter_of_line
                    attack_piece.num_coord = str(val.index(val2) + 1)
                    field_check = attack_piece.letter_coord + attack_piece.num_coord
                    piece_moves = figure_moves(Figure, field_coord, attack_piece, begin_pos)
                    piece_check_info += under_check(Figure, field_coord, piece_moves, field_check, last_move_color)
                    if piece_check_info:
                        print('check by knight', field_check)

        letter_of_line = chr(ord(letter_of_line)+1)
    return piece_check_info

def check_escape_try(Figure, field_coord, defence_piece, attack_piece, begin_pos, last_move_color):
    result = []
    letter_of_line = 'a'
    for val in field_coord.values():
        for val2 in val:
            if val2 != '':
                if val2[0] != last_move_color and val2[1] != 'P' and val2[1] != 'K':
                    defence_piece.color = val2[0]
                    defence_piece.type = val2[1]
                    defence_piece.letter_coord = letter_of_line
                    defence_piece.num_coord = str(val.index(val2) + 1)
                    piece_moves = figure_moves(Figure, field_coord, defence_piece, begin_pos)
                    return_pos = defence_piece.letter_coord + defence_piece.num_coord
                    for j in range(len(piece_moves)):
                        for i in range(len(piece_moves[j])):
                            defence_piece.letter_coord = piece_moves[j][i][0]
                            defence_piece.num_coord = piece_moves[j][i][1]
                            checking_line = line_check(field_coord, defence_piece.letter_coord + defence_piece.num_coord, piece_moves, val2[0])
                            double_check_and_move(field_coord, checking_line, return_pos, defence_piece.letter_coord + defence_piece.num_coord)
                            new_pos_check = position_check_for_checks(Figure, attack_piece, field_coord, begin_pos, last_move_color)
                            if not new_pos_check:
                                if len(new_pos_check) > 1:
                                    for i in new_pos_check:
                                        result.append(i)
                                else:
                                    result.append(return_pos)
                                    result.append(defence_piece.letter_coord + defence_piece.num_coord)
                                    result.append(val2)
                            double_check_and_move(field_coord, checking_line, defence_piece.letter_coord + defence_piece.num_coord, return_pos)

        letter_of_line = chr(ord(letter_of_line)+1)
    return result if result else result.append(False)