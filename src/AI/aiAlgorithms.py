from AI.treeNode import TreeNode
from collections import deque
from model.level import Level
from settings import *
import heapq

visited = set()
depth = 0


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

    if goal_state_func(v.state): return v
    if curr_depth < v.state.max : 
        visited.add(v.state)

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
        return root # TODO check this

    return dfs_depth(root, goal_state_func, operators_func, 0, depth_limit)


def dfs_depth(v, goal_state_func, operators_func, curr_depth, depth_limit):

    if curr_depth > depth_limit: return None

    if goal_state_func(v.state): return v
    
    for state, move in operators_func(v.state):
        child_node = TreeNode(state, move)

        v.add_child(child_node)

        node = dfs_depth(child_node, goal_state_func, operators_func, curr_depth + 1, depth_limit)

        if not node is None : return node

    return None



# Greedy

def search(initial_state, goal_state_func, operators_func, h = lambda _ : 0, W = 1, g = lambda node : node.depth, steps:int = -1):

    f = lambda n: g(n) + h(n.state) * W

    setattr(TreeNode, "__lt__", lambda self, other: f(self) < f(other))

    root = TreeNode(initial_state, depth=0)

    states = [root]
    visited = set() 
    visited.add(initial_state)
    while states:
        node = heapq.heappop(states)
            #print(node.move, node.depth)
        if goal_state_func(node.state):
            return node
        
        if steps == 0:
            return node
        
        if (not node.state.lost()):
        
            for state, move in operators_func(node.state):
                if (not state in visited):

                    child_node = TreeNode(state, move, node.depth + 1)

                    node.add_child(child_node)

                    heapq.heappush(states, child_node)
                    
                    visited.add(state)

        steps -= 1
        
    return None



def breadth_first_search(initial_state, goal_state_func, operators_func):

    return search(initial_state, goal_state_func, operators_func)


def greedy_search(initial_state, goal_state_func, operators_func, heuristic):

    return search(initial_state, goal_state_func, operators_func, h = heuristic, g = lambda _ : 0)


def a_star_search(initial_state, goal_state_func, operators_func, heuristic):

    return search(initial_state, goal_state_func, operators_func, h = heuristic)


def weighted_a_star_search(initial_state, goal_state_func, operators_func, heuristic, weight, steps = -1):

    return search(initial_state, goal_state_func, operators_func, h = heuristic, W = weight, steps = steps)
