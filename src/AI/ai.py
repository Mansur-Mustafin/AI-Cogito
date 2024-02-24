from model.level import Level
from AI.treeNode import TreeNode
from service.analitics import measureTime
import copy


class AI:
    
    def __init__(self, lvl: int, algorithm) -> None:

        self.state = Level(lvl)
        node, self.state.time = measureTime(algorithm, self.state, self.goal_state_func, self.child_states )
        self.moves = node.build_path(node)


    def child_states(self,state) -> list[str]:
        child_states = []

        
        for idx in range(state.get_dimension()):
            if state.is_valid_move('up', idx):
                new_state = copy.deepcopy(state)
                child_states.append((new_state.move_up(idx), f"up {idx}"))

            if state.is_valid_move('right', idx):
                new_state = copy.deepcopy(state)
                child_states.append((new_state.move_right(idx), f"right {idx}"))

            if state.is_valid_move('down', idx):
                new_state = copy.deepcopy(state)
                child_states.append((new_state.move_down(idx), f"down {idx}"))

            if state.is_valid_move('left', idx):
                new_state = copy.deepcopy(state)
                child_states.append((new_state.move_left(idx), f"left {idx}"))
            
        return child_states
    

    def goal_state_func(self, state:Level) -> bool:
        return state.is_win_condition()


