from model.level import Level

def miss_match_heuristic(level:Level):
    return level.count_mismatched_tiles()



def row_collum_miss_match_heuristic(level: Level):
    dim = level.get_dimension()
    res = 0
    for i in range( dim ):
        curr_line = level.get_row_pieces( i)
        target_line = level.get_row_pieces( i)
        curr_col = level.get_col_pieces( i, False)
        target_col = level.get_col_pieces( i, False)
        for color in level.get_main_colors():
            res += abs(target_line[color] - curr_line[color])
            res += abs(target_col[color] - curr_col[color])
    return res + miss_match_heuristic(level)



def manhattan_distance(level:Level):
    res = 0
    
    for cord1, color in level.current_block.items():
        min_dist = 2* level.dimension
        for cord2, color2 in level.target_pattern.items():
            if( color == color2 ):#and not (cord2 in associations)):
                dist = level.manhattan_distance(cord1,cord2)
                if ( min_dist > dist):
                    min_dist = dist
        res += min_dist
    return res
    
def manhattan_distance_with_pattern(level:Level):
        res = 0
        for cord1, color in level.current_block.items():
            min_dist = 2* level.dimension
            for cord2, color2 in level.target_pattern.items():
                if( color == color2 ):#and not (cord2 in associations)):
                    dist = level.manhattan_distance(cord1,cord2)
                    if ( min_dist > dist):
                        min_dist = dist
            res += min_dist
        res +=  pattern(level)

        return res

def pattern(level:Level):
    count = 0
    for l in range(level.dimension):
        line_curr = ['y'] * level.dimension
        line_targ = ['y'] * level.dimension
        for (_, y), color in level.get_board_row(l):
            line_curr [y] = color
        for (_, y), color in level.get_board_row(l, False):
            line_targ [y] = color
        line_curr *=2
        if ''.join(line_targ) in ''.join(line_curr):
            count+=1

    for l in range(level.dimension):
        line_curr = ['y'] * level.dimension
        line_targ = ['y'] * level.dimension
        for (x, _), color in level.get_board_col(l):
            line_curr [x] = color
        for (x, _), color in level.get_board_col(l, False):
            line_targ [x] = color
        line_curr *=2
        if ''.join(line_targ) in ''.join(line_curr):
            count+=1
    return -count * 5 + miss_match_heuristic(level)

    



