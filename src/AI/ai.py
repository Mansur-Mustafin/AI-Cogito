from model.level import Level
from AI.treeNode import TreeNode
from service.analitics import measureTime
import copy
from .aiAlgorithms import *
from .heuristics import *
from enum import Enum, auto

class AIS(Enum):
    BFS = auto()
    DFS = auto()
    IDS = auto()
    GREDDY = auto()
    ASTAR = auto()

class AI:

    ALGORITHMS = {
        AIS.BFS : lambda self :[breadth_first_search, self.state, self.goal_state_func, self.child_states],
        AIS.DFS: lambda self: [depth_first_search, self.state, self.goal_state_func, self.child_states],
        AIS.IDS: lambda self: [iterative_deepening_search, self.state, self.goal_state_func, self.child_states, 1000],
        AIS.GREDDY : lambda self : [ greedy_search, self.state, self.goal_state_func, self.child_states, miss_match_heuristic],
        AIS.ASTAR : lambda self : [ a_star_search, self.state, self.goal_state_func, self.child_states, manhattan_distance_v3]
    }

    def __init__(self, lvl: int, algorithm) -> None:

        self.state = Level(lvl)
        node, self.state.time = measureTime( *self.ALGORITHMS[algorithm](self) )
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


