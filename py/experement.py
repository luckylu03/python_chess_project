begin_pos_init = 16
if begin_pos_init%8 != 0:
    begin_pos = chr(105 - begin_pos_init%8) + str(int(begin_pos_init/8)+1)
else:
    begin_pos = chr(97 + begin_pos_init%8) + str(int(begin_pos_init/8))

print(begin_pos)