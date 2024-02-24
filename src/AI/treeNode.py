class TreeNode:
    def __init__(self, state, move = None, depth = None):
        self.state = state
        self.parent = None
        self.children = []
        self.move = move
        self.depth = depth


    def add_child(self, child_node):
        self.children.append(child_node)
        child_node.parent = self


    def build_path(self, node) -> list[str]:
        if node.parent is None:
            return []

        return self.build_path(node.parent) + [node.move]
