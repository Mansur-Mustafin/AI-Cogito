class TreeNode:
    """
    This class represents a node in a tree data structure.
    It is used to represent a state in a state-space search tree

    Attributes:
    ----------
        state: The state associated with this node.
        parent: The parent TreeNode of this node. None if this is the root node.
        children: A list of TreeNode objects that are children of this node.
        move: The move or action that led to this state from the parent state.
        depth: The depth of this node in the tree.
    """
    def __init__(self, state, move=None, depth=None):
        """
        :param state: The state associated with the node.
        :param move: The move that led to this state from the parent, defaults to None.
        :param depth: The depth of the node in the tree, defaults to None.
        """
        self.state = state
        self.parent = None
        self.children = []
        self.move = move
        self.depth = depth

    def add_child(self, child_node) -> None:
        """
        :param child_node: The child TreeNode to be added.
        """
        self.children.append(child_node)
        child_node.parent = self

    def build_path(self, node) -> list[str]:
        """
        Constructs a path from the root node to the given node.
        :param node: The node to build the path to.
        :return: A list of moves
        :rtype: list[str]
        """
        if node.parent is None:
            return []

        return self.build_path(node.parent) + [node.move]
