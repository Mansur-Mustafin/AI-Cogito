from model.level import Level

def miss_match_heuristic(level:Level):
    return level.count_mismatched_tiles()



def row_collum_miss_match_heuristic(level: Level):
    dim = level.get_dimension()
    res = 0
    for i in range( dim ):
        curr_line = get_row_pieces(level.COLORS, i ,level.get_current_board() )
        target_line = get_row_pieces(level.COLORS, i ,level.get_target_board() )
        curr_col = get_col_pieces(level.COLORS, i ,level.get_current_board() )
        target_col = get_col_pieces(level.COLORS, i ,level.get_target_board() )
        for color in level.COLORS.keys():
            res += abs(target_line[color] - curr_line[color])
            res += abs(target_col[color] - curr_col[color])
    return res

def get_row_pieces(Colors, idx, board) -> dict:
    colors_freq = {color : 0 for color in Colors}

    for cell in board[idx]:
        if cell != 'y':
            colors_freq[cell] += 1
    
    return colors_freq

def get_col_pieces(Colors, idx, board) -> dict:
    colors_freq = {color : 0 for color in Colors}

    for row in board:
        if row[idx] != 'y':
            colors_freq[row[idx]] += 1

    return colors_freq