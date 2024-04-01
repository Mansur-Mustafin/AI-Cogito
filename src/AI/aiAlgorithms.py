from AI.treeNode import TreeNode
from collections import deque
from model.level import Level
from settings import *
import heapq
from typing import Callable

visited = set()
depth = 0


# DFS

def depth_first_search(initial_state: Level, goal_state_func: Callable[Level, bool], operators_func: Callable[Level, list[Level]]) -> TreeNode:
    """
    Implements a generic Depth-First Search algorithm
    :param initial_state: Initial state of the problem
    :type initial_state: Level
    :param goal_state_func: Function that evaluates if the game has ended
    :type goal_state_func: Callable[Level, bool]
    :param operators_func: Function that returns a list of the possible next Level states according to the possible moves
    :type operators_func: Callable[Level, list[Level]]
    :return: Node of the solution to the problem
    :rtype: TreeNode
    """

    global visited
    visited = set()

    root = TreeNode(initial_state)

    if goal_state_func(initial_state):
        return initial_state
    
    node = dfs(root, goal_state_func, operators_func, 0)

    return node



def dfs(v: TreeNode, goal_state_func: Callable[Level, bool], operators_func: Callable[Level, list[Level]], curr_depth: int) -> TreeNode:
    """
    Implements a cycle of a generic Depth-First Search algorithm
    :param v: Node we are currently visiting
    :type v: TreeNode
    :param goal_state_func: Function that evaluates if the game has ended
    :type goal_state_func: Callable[Level, bool]
    :param operators_func: Function that returns a list of the possible next Level states according to the possible moves
    :type operators_func: Callable[Level, list[Level]]
    :param curr_depth: Depth of the node we are currently visiting in the tree
    :type curr_depth: int
    :return: Node of the solution to the problem
    :rtype: TreeNode
    """

    if goal_state_func(v.state): return v
    if curr_depth < v.state.max : 
        visited.add(v.state)

        for state, move in operators_func(v.state):
            if not state in visited:
                child_node = TreeNode(state, move)

                v.add_child(child_node)

                node = dfs(child_node, goal_state_func, operators_func, curr_depth + 1)

                if not node is None : return node


def iterative_deepening_search(initial_state: Level, goal_state_func: Callable[Level, bool],
                               operators_func: Callable[Level, list[Level]], depth_limit: int) -> TreeNode:
    """
    Implements a generic Iterative Deepening Search algorithm
    :param initial_state: Initial state of the problem
    :type initial_state: Level
    :param goal_state_func: Function that evaluates if the game has ended
    :type goal_state_func: Callable[Level, bool]
    :param operators_func: Function that returns a list of the possible next Level states according to the possible moves
    :type operators_func: Callable[Level, list[Level]]
    :param depth_limit: Maximum depth of the search tree
    :type depth_limit: int
    :return: Node of the solution to the problem
    :rtype: TreeNode
    """

    node = None
    curr_limit_depth = 0 

    while (node is None) and curr_limit_depth <= depth_limit:
        node = depth_limited_search(initial_state, goal_state_func, operators_func, curr_limit_depth)

        curr_limit_depth += 1

    return node


def depth_limited_search(initial_state: Level, goal_state_func: Callable[Level, bool],
                               operators_func: Callable[Level, list[Level]], depth_limit: int) -> TreeNode:
    """
    Implements a cycle for a generic Iterative Deepening Search algorithm
    :param initial_state: Initial state of the problem
    :type initial_state: Level
    :param goal_state_func: Function that evaluates if the game has ended
    :type goal_state_func: Callable[Level, bool]
    :param operators_func: Function that returns a list of the possible next Level states according to the possible moves
    :type operators_func: Callable[Level, list[Level]]
    :param depth_limit: Maximum depth of the search tree
    :type depth_limit: int
    :return: Node of the solution to the problem
    :rtype: TreeNode
    """
    root = TreeNode(initial_state)

    if goal_state_func(initial_state):
        return root

    return dfs_depth(root, goal_state_func, operators_func, 0, depth_limit)


def dfs_depth(v: TreeNode, goal_state_func: Callable[Level, bool], operators_func: Callable[Level, list[Level]],
              curr_depth: int, depth_limit: int) -> TreeNode:
    """
    Implements a cycle of a generic Depth-First Search algorithm up to a certain depth
    :param v: Node we are currently visiting
    :type v: TreeNode
    :param goal_state_func: Function that evaluates if the game has ended
    :type goal_state_func: Callable[Level, bool]
    :param operators_func: Function that returns a list of the possible next Level states according to the possible moves
    :type operators_func: Callable[Level, list[Level]]
    :param curr_depth: Depth of the node we are currently visiting in the tree
    :type curr_depth: int
    :param depth_limit: Maximum depth of the search tree
    :type depth_limit: int
    :return: Node of the solution to the problem
    :rtype: TreeNode
    """
    if curr_depth > depth_limit: return None

    if goal_state_func(v.state): return v
    
    for state, move in operators_func(v.state):
        child_node = TreeNode(state, move)

        v.add_child(child_node)

        node = dfs_depth(child_node, goal_state_func, operators_func, curr_depth + 1, depth_limit)

        if not node is None : return node

    return None



# Greedy

def search(initial_state: Level, goal_state_func: Callable[Level, bool], operators_func: Callable[Level, list[Level]],
           h: Callable[Level, int] = lambda _ : 0, W: int = 1, g: Callable[TreeNode, int] = lambda node : node.depth,
           steps: int = -1) -> TreeNode:
    """
    Implements the BFS, Greedy, A* or weighted A* algorithms depending on the values passed in the variables h, W and g,
    that represent the estimated cost to reach the objective, that is defined by the heuristic that is used, the weight
    given to the result of function h, and the total cost to reach the current node, respectively. Below is the
    association of the algorithms to the possible values of h, W and g.

    - BFS: h(node) = 0, W doesn't matter (W = 0), g(node) = node.depth
    - Greedy: h(node) = heuristic(node), W = 1, g(node) = 0
    - A*: h(node) = heuristic(node), W = 1, g(node) = node.depth
    - Weighted A*: h(node) = heuristic(node), W = some integer, g(node) = node.depth

    :param initial_state: Initial state of the problem
    :type initial_state: Level
    :param goal_state_func: Function that evaluates if the game has ended
    :type goal_state_func: Callable[Level, bool]
    :param operators_func: Function that returns a list of the possible next Level states according to the possible moves
    :type operators_func: Callable[Level, list[Level]]
    :param h: Heuristic function to be used by the AI
    :type h: Callable[Level, int]
    :param W: Weight of the heuristic function to find the solution
    :type W: int
    :param g: Function to evaluate total cost to the current node
    :type g: Callable[TreeNode, int]
    :param steps: Limit of steps to take in the algorithm
    :type steps: int
    :return: Node of the solution to the problem
    :rtype: TreeNode
    """

    f = lambda n: g(n) + h(n.state) * W
    setattr(TreeNode, "__lt__", lambda self, other: f(self) < f(other))

    root = TreeNode(initial_state, depth=0)
    states = [root]
    visited = set() 
    visited.add(initial_state)
    while states:
        node = heapq.heappop(states)
        if goal_state_func(node.state):
            return node
        
        if steps == 0:
            return node
        
        if (not node.state.lost()):
        
            for state, move in operators_func(node.state):
                if (not state in visited):
                    
                    state.increment_score()
                    child_node = TreeNode(state, move, node.depth + 1)

                    node.add_child(child_node)

                    heapq.heappush(states, child_node)
                    
                    visited.add(state)

        steps -= 1
        
    return None



def breadth_first_search(initial_state: Level, goal_state_func: Callable[Level, bool], operators_func: Callable[Level, list[Level]]) -> TreeNode:
    """
    Implements a generic Breadth-First Search algorithm
    :param initial_state: Initial state of the problem
    :type initial_state: Level
    :param goal_state_func: Function that evaluates if the game has ended
    :type goal_state_func: Callable[Level, bool]
    :param operators_func: Function that returns a list of the possible next Level states according to the possible moves
    :type operators_func: Callable[Level, list[Level]]
    :return: Node of the solution to the problem
    :rtype: TreeNode
    """
    return search(initial_state, goal_state_func, operators_func)


def greedy_search(initial_state: Level, goal_state_func: Callable[Level, bool], operators_func: Callable[Level, list[Level]],
                  heuristic) -> TreeNode:
    """
    Implements a generic Greedy search algorithm using a certain heuristic
    :param initial_state: Initial state of the problem
    :type initial_state: Level
    :param goal_state_func: Function that evaluates if the game has ended
    :type goal_state_func: Callable[Level, bool]
    :param operators_func: Function that returns a list of the possible next Level states according to the possible moves
    :type operators_func: Callable[Level, list[Level]]
    :param heuristic: Heuristic to be used
    :type heuristic: enum H
    :return: Node of the solution to the problem
    :rtype: TreeNode
    """
    return search(initial_state, goal_state_func, operators_func, h = heuristic, g = lambda _ : 0)


def a_star_search(initial_state: Level, goal_state_func: Callable[Level, bool], operators_func: Callable[Level, list[Level]],
                  heuristic) -> TreeNode:
    """
    Implements a generic A* search algorithm using a certain heuristic
    :param initial_state: Initial state of the problem
    :type initial_state: Level
    :param goal_state_func: Function that evaluates if the game has ended
    :type goal_state_func: Callable[Level, bool]
    :param operators_func: Function that returns a list of the possible next Level states according to the possible moves
    :type operators_func: Callable[Level, list[Level]]
    :param heuristic: Heuristic to be used
    :type heuristic: enum H
    :return: Node of the solution to the problem
    :rtype: TreeNode
    """
    return search(initial_state, goal_state_func, operators_func, h = heuristic)


def weighted_a_star_search(initial_state: Level, goal_state_func: Callable[Level, bool], operators_func: Callable[Level, list[Level]],
                  heuristic, weight: int, steps: int = -1):
    """
    Implements a generic weighted A* search algorithm using a certain heuristic
    :param initial_state: Initial state of the problem
    :type initial_state: Level
    :param goal_state_func: Function that evaluates if the game has ended
    :type goal_state_func: Callable[Level, bool]
    :param operators_func: Function that returns a list of the possible next Level states according to the possible moves
    :type operators_func: Callable[Level, list[Level]]
    :param heuristic: Heuristic to be used
    :type heuristic: enum H
    :param weight: Weight attributed to the heuristic in the A* algorithm
    :type weight: int
    :param steps: Limit of steps to take in the algorithm
    :type steps: int
    :return: Node of the solution to the problem
    :rtype: TreeNode
    """
    return search(initial_state, goal_state_func, operators_func, h = heuristic, W = weight, steps = steps)
