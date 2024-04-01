from model.level import Level


def miss_match_heuristic(level: Level) -> int:
    """
    :param level: state of the level to evaluate
    :type level: Level
    :return: The number of tiles that aren't in the correct place in regards to the target board
    :rtype: int
    """
    return level.count_mismatched_tiles()


def row_column_miss_match_heuristic(level: Level) -> int:
    """
    :param level: state of the level to evaluate
    :type level: Level
    :return: The sum of missmatched tiles of every row and column of the board
    :rtype: int
    """
    dim = level.get_dimension()
    res = 0
    for i in range(dim):
        curr_line = level.get_row_pieces(i)
        target_line = level.get_row_pieces(i)
        curr_col = level.get_col_pieces(i, False)
        target_col = level.get_col_pieces(i, False)
        for color in level.get_main_colors():
            res += abs(target_line[color] - curr_line[color])
            res += abs(target_col[color] - curr_col[color])
    return res


def manhattan_distance(level: Level) -> int:
    """
    :param level: state of the level to evaluate
    :type level: Level
    :return: The sum of the manhattan distances of every tile in the current board
        to the closest valid tile in the target board
    :rtype: int
    """
    res = 0

    for cord1, color in level.current_block.items():
        min_dist = 2 * level.dimension
        for cord2, color2 in level.target_pattern.items():
            if color == color2:
                dist = level.manhattan_distance(cord1, cord2)
                if min_dist > dist:
                    min_dist = dist
        res += min_dist
    return res


def pattern(level: Level) -> int:
    """
    A row (or column) in the correct pattern is a row that only needs to be shifted right/left
    (up/down if it is a column) to be in the correct position.
    :param level: state of the level to evaluate
    :type level: Level
    :return: The sum of the missmatch heuristic with the negative value of the number
        of rows and columns that have the correct pattern in comparison to the target board.
    :rtype: int
    """

    count = 0
    for l in range(level.dimension):
        line_curr = ['y'] * level.dimension
        line_targ = ['y'] * level.dimension
        for (_, y), color in level.get_board_row(l):
            line_curr[y] = color
        for (_, y), color in level.get_board_row(l, False):
            line_targ[y] = color
        line_curr *= 2
        if ''.join(line_targ) in ''.join(line_curr):
            count += 1

    for l in range(level.dimension):
        line_curr = ['y'] * level.dimension
        line_targ = ['y'] * level.dimension
        for (x, _), color in level.get_board_col(l):
            line_curr[x] = color
        for (x, _), color in level.get_board_col(l, False):
            line_targ[x] = color
        line_curr *= 2
        if ''.join(line_targ) in ''.join(line_curr):
            count += 1
    return -count * 5 + level.count_mismatched_tiles()


def manhattan_distance_with_pattern(level: Level) -> int:
    """
    This particular heuristic mixes the pattern and manhattan distance heuristics to 
    achieve better results
    :param level: state of the level to evaluate
    :type level: Level
    :return: The sum between the manhattan and pattern heuristics
    :rtype: int
    """

    res = manhattan_distance(level) + pattern(level)
    return res
