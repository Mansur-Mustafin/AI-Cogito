from model.level import Level

def miss_match_heuristic(level:Level):
    return level.count_mismatched_tiles()



def row_collum_miss_match_heuristic(level: Level):
    dim = level.get_dimension()
    res = 0
    for i in range( dim ):
        curr_line = get_row_pieces(level.get_main_colors(), level.get_board_row(i))
        target_line = get_row_pieces(level.get_main_colors(), level.get_board_col(i))
        curr_col = get_col_pieces(level.get_main_colors(), level.get_board_row(i, False))
        target_col = get_col_pieces(level.get_main_colors(), level.get_board_col(i, False))
        for color in level.get_main_colors():
            res += abs(target_line[color] - curr_line[color])
            res += abs(target_col[color] - curr_col[color])
    return res

def get_row_pieces(colors, row) -> dict:
    colors_freq = {color: 0 for color in colors}

    for cell in row:
        if cell[1] != 'y':
            colors_freq[cell[1]] += 1
    
    return colors_freq

def get_col_pieces(colors, col) -> dict:
    colors_freq = {color: 0 for color in colors}

    for cell in col:
        if cell[1] != 'y':
            colors_freq[cell[1]] += 1

    return colors_freq
