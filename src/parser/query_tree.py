def build_query_tree(query):
    # Your implementation here
    # Parse the SQL query and build a query tree
    # For now, return a placeholder
    return {"parsed_query": query, "tree": {}}
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def __repr__(self):
        return f"{self.value}({', '.join(str(c) for c in self.children)})"

class TableNode(TreeNode):
    pass

class SelectionNode(TreeNode):
    pass

class ProjectionNode(TreeNode):
    pass

class JoinNode(TreeNode):
    pass