from AI.treeNode import TreeNode
from collections import deque
from model.level import Level
import heapq

visited = set()
depth = 0

# BFS

def breadth_first_search(initial_state, goal_state_func, operators_func):
    global visited
    visited.add(initial_state)
    visited = set()
    root = TreeNode(initial_state)  
    queue = deque([root])   
    while queue:
        node = queue.popleft() 
        visited.add(node.state)
        if goal_state_func(node.state):   
            return node

        for state, move in operators_func(node.state):
            if not state in visited:

                child_node = TreeNode(state, move)
            
                node.add_child(child_node)

                queue.append(child_node)

    return None


# DFS



def depth_first_search(initial_state, goal_state_func, operators_func):

    global visited
    visited = set()

    root = TreeNode(initial_state)

    if goal_state_func(initial_state):
        return initial_state
    
    node = dfs(root, goal_state_func, operators_func, 0)

    return node



def dfs(v, goal_state_func, operators_func, curr_depth):
    visited.add(v.state)

    if goal_state_func(v.state):
        global depth 
        depth = curr_depth
        return v
    
    for state, move in operators_func(v.state):
        if not state in visited:
            child_node = TreeNode(state, move)

            v.add_child(child_node)

            node = dfs(child_node, goal_state_func, operators_func, curr_depth + 1)

            if not node is None : return node


# IDS

def iterative_deepening_search(initial_state, goal_state_func, operators_func, depth_limit):
    node = None
    curr_limit_depth = 0 
    

    while (node is None) and curr_limit_depth <= depth_limit: 

        print(f"curr_limit_depth = {curr_limit_depth}")

        node = depth_limited_search(initial_state, goal_state_func, operators_func, curr_limit_depth)

        curr_limit_depth += 1

    return node


def depth_limited_search(initial_state, goal_state_func, operators_func, depth_limit):

    root = TreeNode(initial_state)

    if goal_state_func(initial_state):
        return initial_state

    node = dfs_depth(root, goal_state_func, operators_func, 0, depth_limit)

    return node
    

def dfs_depth(v, goal_state_func, operators_func, curr_depth, depth_limit):

    if goal_state_func(v.state) and curr_depth <= depth_limit:
        global depth 
        depth = curr_depth
        return v
    
    if curr_depth > depth_limit: return None
    
    for state, move in operators_func(v.state):
        child_node = TreeNode(state, move)

        v.add_child(child_node)

        node = dfs_depth(child_node, goal_state_func, operators_func, curr_depth + 1, depth_limit)

        if not node is None : return node


### Greedy

def greedy_search(initial_state, goal_state_func, operators_func, heuristic):

    setattr(TreeNode, "__lt__", lambda self, other: heuristic(self.state) < heuristic(other.state))

    root = TreeNode(initial_state, depth=0)

    states = [root]
    visited = set() 
    visited.add(initial_state)

    while states:

        node = heapq.heappop(states)

        if goal_state_func(node.state):
            return node
        
        for state, move in operators_func(node.state):
            if not state in visited:

                child_node = TreeNode(state, move, node.depth + 1)

                node.add_child(child_node)

                heapq.heappush(states, child_node)

                visited.add(child_node)
        
    return None



### A*

def a_star_search(initial_state, goal_state_func, operators_func, heuristic):

    g_func = lambda node : heuristic(node.state) + node.depth

    return greedy_search(initial_state, goal_state_func, operators_func, g_func)
