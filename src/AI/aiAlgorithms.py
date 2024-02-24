from AI.treeNode import TreeNode
from collections import deque



def breadth_first_search(initial_state, goal_state_func, operators_func):
    root = TreeNode(initial_state)  
    queue = deque([root])   
    while queue:
        node = queue.popleft()  
        if goal_state_func(node.state):   
            return node

        for state, move in operators_func(node.state):

            child_node = TreeNode(state, move)
            
            node.add_child(child_node)

            queue.append(child_node)

    return None
