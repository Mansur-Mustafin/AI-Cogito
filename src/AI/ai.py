import copy
from enum import Enum, auto
from typing import Callable

from .aiAlgorithms import *
from .heuristics import *
from service.analitics import measure_performance


# TODO: Should this enum be moved to setting.py?
class AIS(Enum):
    """
    An enumeration of different Artificial Intelligence Search (AIS) algorithms.

    Attributes:
    ----------
        BFS: the Breadth-First Search algorithm.
        DFS: the Depth-First Search algorithm.
        IDS: the Iterative Deepening Search algorithm.
        GREDDY: the Greedy Search algorithm.
        ASTAR: the A* Search algorithm.
        ASTARW: the Weighted A* Search algorithm.
    """
    BFS = auto()
    DFS = auto()
    IDS = auto()
    GREDDY = auto()
    ASTAR = auto()
    ASTARW = auto()


class H(Enum):
    """
    An enumeration of different heuristics that is used in heuristic-based search algorithms.

    Attributes:
    ----------
        MISS: Represents a Piece Mismatches heuristic.
        MANHATTAN: Represents the Manhattan Distance heuristic.
        PATTERN: Represents a Correct Row Pattern heuristic.
        LINECOLUMN: Represents a Line and Columns Difference heuristic.
        MANHATTAN_PATTERN: Represents a combined heuristic of Manhattan Distance and Correct Row Pattern heuristic.
    """
    MISS = auto()
    MANHATTAN = auto()
    PATTERN = auto()
    LINECOLUMN = auto()
    MANHATTAN_PATTERN = auto()


class AI:
    """
    A class representing the Artificial Intelligence (AI) for solving a Cogito game.

    Attributes:
    ----------
        state: The current level (board).
        weight: The weight used in Weighted A* Search algorithm.
        steps: The limit number of steps, in cases when user use 'Help' button.
        heuristic: The heuristic function used in search algorithms.
        moves: A list of moves that leads from the initial state to the goal state.
    """

    ALGORITHMS = {
        AIS.BFS: lambda self: [breadth_first_search, self.state, self.goal_state_func, self.child_states],
        AIS.DFS: lambda self: [depth_first_search, self.state, self.goal_state_func, self.child_states],
        AIS.IDS: lambda self: [iterative_deepening_search, self.state, self.goal_state_func, self.child_states, 1000],
        AIS.GREDDY: lambda self: [greedy_search, self.state, self.goal_state_func, self.child_states, self.heuristic],
        AIS.ASTAR: lambda self: [a_star_search, self.state, self.goal_state_func, self.child_states, self.heuristic],
        AIS.ASTARW: lambda self: [weighted_a_star_search, self.state, self.goal_state_func, self.child_states,
                                  self.heuristic, self.weight, self.steps]
    }

    def __init__(self, level: Level, algorithm, heuristic=None, weight=1, steps=-1) -> None:
        """
        Initializes the AI with the specified level, algorithm, and optional heuristic, weight, and steps.

        :param level: The current level.
        :param algorithm: The algorithm to use for solving the puzzle.
        :param heuristic: Optional heuristic for informed search algorithms.
        :param weight: The weight factor for Weighted A* Search algorithm, default is 1.
        :param steps: The limit number of steps, in cases when user use 'Help' button.
        """
        self.state = level
        self.weight = weight
        self.steps = steps
        self.heuristic = self._map_heuristic(heuristic)
        node, self.state.time, self.memory = measure_performance(*self.ALGORITHMS[algorithm](self))
        self.moves = node.build_path(node)

    def child_states(self, state: Level) -> list[tuple[Level, str]]:
        """
        Generates a list of possible child states from the current state.

        :param state: The current state of the game.
        :return: A list of child states and their corresponding moves.
        """
        child_states = []

        for idx in range(state.get_dimension()):
            # The repetition of the definition of the variable new_state is necessary!

            if sum(state.get_col_pieces(idx).values()) > 0:
                new_state = copy.deepcopy(state)
                child_states.append((new_state.move_col(idx, -1), f"up {idx}"))
                new_state = copy.deepcopy(state)
                child_states.append((new_state.move_col(idx, 1), f"down {idx}"))

            if sum(state.get_row_pieces(idx).values()) > 0:
                new_state = copy.deepcopy(state)
                child_states.append((new_state.move_row(idx, 1), f"right {idx}"))

                new_state = copy.deepcopy(state)
                child_states.append((new_state.move_row(idx, -1), f"left {idx}"))

        return child_states

    def goal_state_func(self, state: Level) -> bool:
        """
        Check winning condition of game.

        :param state: The state to be evaluated.
        :return: True if it's a goal state, False otherwise.
        """
        return state.is_win_condition()

    def _map_heuristic(self, heuristic: Enum) -> Callable[[Level], int] | None:
        """
        Maps the given heuristic enum to its corresponding function.

        :param heuristic: The heuristic to be used.
        :return: The corresponding heuristic function.
        """
        if heuristic == H.MISS:
            return miss_match_heuristic
        elif heuristic == H.LINECOLUMN:
            return row_collum_miss_match_heuristic
        elif heuristic == H.MANHATTAN:
            return manhattan_distance
        elif heuristic == H.PATTERN:
            return pattern
        elif heuristic == H.MANHATTAN_PATTERN:
            return manhattan_distance_with_pattern
        else:
            return None
