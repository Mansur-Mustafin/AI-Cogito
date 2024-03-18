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
    return res

def manhattan_distance(level:Level):
    dist = 0
    for cord, (_, id) in level.current_block.items():
        dist += level.manhattan_distance(cord, level.associated_pieces[id])
    return dist

def manhattan_distance_v2(level:Level):
        i = 0 
        res = 0
        associations = []
        for cord1, (color, _) in level.current_block.items():
            associations.append((0,0))
            min_dist = 2* level.dimension
            for cord2, (color2, _) in level.target_pattern.items():
                if( color == color2 and not (cord2 in associations)):
                    dist = level.manhattan_distance(cord1,cord2)
                    if ( min_dist > dist):
                        min_dist = dist
                        associations[i]= cord2
            i+=1
            res += min_dist
        return res
    
def manhattan_distance_v3(level:Level):
        i = 0 
        res = 0
        associations = []
        for cord1, (color, _) in level.current_block.items():
            associations.append((0,0))
            min_dist = 2* level.dimension
            for cord2, (color2, _) in level.target_pattern.items():
                if( color == color2 and not (cord2 in associations)):
                    dist = level.manhattan_distance(cord1,cord2)
                    if ( min_dist > dist):
                        min_dist = dist
                        associations[i]= cord2
            i+=1
            res += min_dist
            res +=   miss_match_heuristic(level)
        return res

def manhattan_distance_v4(level:Level):
    dist = 0
    for cord, (_, id) in level.current_block.items():
        dist += level.manhattan_distance(cord, level.associated_pieces[id])
    
    return dist + miss_match_heuristic(level)

