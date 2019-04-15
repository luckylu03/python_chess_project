def line_check(field_coord, end_pos, piece_moves, last_move_color):
    checking_line = {}
    if last_move_color == 'W':
        enemy_color = 'B'
    else:
        enemy_color = 'W'
    if end_pos in piece_moves:
        print(end_pos)
        if field_coord[end_pos[0]][int(end_pos[1])-1] == '':
            checking_line[end_pos] = 'ok'
        elif field_coord[end_pos[0]][int(end_pos[1])-1][0] != enemy_color:
            checking_line[end_pos] = 'enemy'
        elif field_coord[end_pos[0]][int(end_pos[1])-1][0] != enemy_color and field_coord[end_pos[0]][int(end_pos[1])-1][0] == 'K':
            checking_line[end_pos] = 'check'
        elif field_coord[end_pos[0]][int(end_pos[1])-1][0] != last_move_color:
            checking_line[end_pos] = 'block'
    elif end_pos in [end_pos for i in range(len(piece_moves)) if end_pos in piece_moves[i]]:
        for direction in range(len(piece_moves)):
            if end_pos in piece_moves[direction]:
                for x in piece_moves[direction][:piece_moves[direction].index(end_pos)+1]:
                    if x != end_pos:
                        if field_coord[x[0]][int(x[1])-1] == '':
                            checking_line[x] = 'ok'
                        elif field_coord[x[0]][int(x[1])-1][len(field_coord[x[0]][int(x[1])-1])-1] == 'K':
                            if field_coord[x[0]][int(x[1])-1][len(field_coord[x[0]][int(x[1])-1])-2] == enemy_color:
                                checking_line[x] = 'check'
                            else:
                                checking_line[x] = 'block'
                        else:
                            checking_line[x] = 'block'
                    elif x == end_pos:
                        if field_coord[x[0]][int(x[1])-1] == '':
                            checking_line[x] = 'ok'
                        elif field_coord[x[0]][int(x[1])-1][len(field_coord[x[0]][int(x[1])-1])-1] == 'K':
                            if field_coord[x[0]][int(x[1])-1][len(field_coord[x[0]][int(x[1])-1])-2] == enemy_color:
                                checking_line[x] = 'check'
                            else:
                                checking_line[x] = 'block'
                        elif field_coord[x[0]][int(x[1])-1][0] == enemy_color:
                            checking_line[x] = 'enemy'
                        else:
                            checking_line[x] = 'block'
    return checking_line
