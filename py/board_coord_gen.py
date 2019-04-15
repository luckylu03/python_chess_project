def coord_gen():
    field_coord = {}

    for i in [chr(x) for x in range(97, 105)]:
        field_coord[i] = ["" for x in range(1,9)]

    for i in [chr(x) for x in range(97, 105)]:
        field_coord[i][1] = 'WP'
        field_coord[i][6] = 'BP'

    field_coord['a'][0], field_coord['h'][0] = 'WR', 'WR'
    field_coord['a'][7], field_coord['h'][7] = 'BR', 'BR'
    field_coord['b'][0], field_coord['g'][0] = 'WKn', 'WKn'
    field_coord['b'][7], field_coord['g'][7] = 'BKn', 'BKn'
    field_coord['c'][0], field_coord['f'][0] = 'WB', 'WB'
    field_coord['c'][7], field_coord['f'][7] = 'BB', 'BB'
    field_coord['e'][0], field_coord['e'][7] = 'WK', 'BK'
    field_coord['d'][0], field_coord['d'][7] = 'WQ', 'BQ'
    return field_coord