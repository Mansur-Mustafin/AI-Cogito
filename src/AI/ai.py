from model.level import Level
from AI.treeNode import TreeNode
from service.analitics import measure_performance
import copy
from .aiAlgorithms import *
from .heuristics import *
from enum import Enum, auto

# TODO: Should this enum be moved to setting.py?
class AIS(Enum):
    BFS = auto()
    DFS = auto()
    IDS = auto()
    GREDDY = auto()
    ASTAR = auto()
    ASTARW = auto()

class H(Enum):
    MISS = auto()
    MANHATTAN = auto()
    PATTERN = auto()
    LINECOLUMN = auto()

class AI:

    ALGORITHMS = {
        AIS.BFS : lambda self :[breadth_first_search, self.state, self.goal_state_func, self.child_states],
        AIS.DFS: lambda self: [depth_first_search, self.state, self.goal_state_func, self.child_states],
        AIS.IDS: lambda self: [iterative_deepening_search, self.state, self.goal_state_func, self.child_states, 1000],
        AIS.GREDDY : lambda self : [ greedy_search, self.state, self.goal_state_func, self.child_states, self.heuristic],
        AIS.ASTAR : lambda self : [ a_star_search, self.state, self.goal_state_func, self.child_states, self.heuristic],
        AIS.ASTARW : lambda self : [ weighted_a_star_search, self.state, self.goal_state_func, self.child_states, self.heuristic, self.weight, self.steps]
    }

    def __init__(self, level : Level, algorithm, heuristic = None, weight = 1, steps = -1) -> None:

        self.state = level
        self.weight = weight
        self.steps = steps
        self.heuristic = self._map_heuristic(heuristic)
        node, self.state.time, self.memory = measure_performance( *self.ALGORITHMS[algorithm](self) )
        self.moves = node.build_path(node)


    def child_states(self,state:Level) -> list[str]:
        child_states = []

        
        for idx in range(state.get_dimension()):
            # The repetition of the definition of the variable new_state is necessary!

            if(sum(state.get_col_pieces(idx).values())>0):
                new_state = copy.deepcopy(state)
                child_states.append((new_state.move_col(idx, -1), f"up {idx}"))
                new_state = copy.deepcopy(state)
                child_states.append((new_state.move_col(idx, 1), f"down {idx}"))

            if(sum(state.get_row_pieces(idx).values())>0):
                new_state = copy.deepcopy(state)
                child_states.append((new_state.move_row(idx, 1), f"right {idx}"))

                new_state = copy.deepcopy(state)
                child_states.append((new_state.move_row(idx, -1), f"left {idx}"))

            
        return child_states
    

    def goal_state_func(self, state:Level) -> bool:
        return state.is_win_condition()

    def _map_heuristic(self, heuristic):
        if heuristic == H.MISS:
            return miss_match_heuristic
        elif heuristic == H.LINECOLUMN:
            return row_collum_miss_match_heuristic
        elif heuristic == H.MANHATTAN:
            return manhattan_distance_v3
        elif heuristic == H.PATTERN:
            return pattern
        else:
            return None
